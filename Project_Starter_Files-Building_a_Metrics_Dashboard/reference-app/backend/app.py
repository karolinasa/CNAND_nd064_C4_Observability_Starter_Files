from flask import Flask, render_template, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from os import getenv
from jaeger_client import Config
import logging
import pymongo
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'
mongo = PyMongo(app)
JAEGER_HOST = getenv('JAEGER_HOST', 'localhost')
metrics = PrometheusMetrics(app)

metrics.info("app_info", "Application info", version="1.0.3")

metrics.register_default(
    metrics.counter(
        'by_endpoint_counter', 'Request count by request endpoint',
        labels={'endpoint': lambda: request.endpoint}
    )
)


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
            'local_agent': {
                'reporting_host': JAEGER_HOST
            }
        },
        service_name=service,
    )

    return config.initialize_tracer()


tracer = init_tracer('backend-service')


@app.route('/')
def homepage():
    with tracer.start_span('backend-homepage') as span:
        result = 'Hello World'
        span.set_tag('output', result)
        return result


@app.route('/api')
def my_api():
    with tracer.start_span('backend-api') as span:
        answer = 'something'
        result = jsonify(response=answer)
        span.set_tag('output', result)
        return result


@app.route('/star', methods=['POST'])
def add_star():
    with tracer.start_span('backend-star') as span:
        try:
            star = mongo.db.stars
            name = request.json['name']
            distance = request.json['distance']
            star_id = star.insert({'name': name, 'distance': distance})
            new_star = star.find_one({'_id': star_id })

            output = {'name' : new_star['name'], 'distance' : new_star['distance']}
            result = jsonify({'result' : output})
            span.set_tag('output', result)
            return result
        except Exception as e:
            error_message  = 'Failed to insert record. Error message: %s' % e.args[0]
            span.set_tag('output', error_message)


if __name__ == "__main__":
    app.run()
    
