**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

Run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

Pods: 

[Namespace: default](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/pods-default.png) 

[Namespace: monitoring](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/pods-monitoring.png) 

[Namespace: observability](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/pods-observability.png)

Services: 

[All services](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/services.png)

## Setup the Jaeger and Prometheus source
Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

[Grafana homepage](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana-homepage.png)

[Grafana data sources](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana-data-sources.png)

## Create a Basic Dashboard
Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

To create a dashboard I used a reference dashboard in the [project repository](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/reference-dashboards/kubernetes-cluster-monitoring-via-prometheus_rev3.json).

[Basic Grafana Dashboard with Prometheus as a source](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/prometheus-datasource-reference-dashboard.png)

## Describe SLO/SLI
SLOs of *monthly uptime* and *request response time* are:
- Application uptime will be 99.9% in a month
- 99% of requests will reply within 250 ms of receiving a request in a month

Based on SLOs of *monthly uptime* and *request response time* defined, SLIs are:
- Last month application uptime was 99.95%
- Last month 99.2% of requests replied within 250 ms of receiving a request


## Creating SLI metrics.
It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs.

Metrics to measure SLIs defined:
- The time in ms to reply to a request
- The number of requests received per second
- The number of failed requests (40x and 50x responses)
- The percentage of CPU used
- The application uptime (both front-end and back-end applications)


## Create a Dashboard to measure our SLIs
Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

[Uptime (24h)](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/uptime.png) 

[HTTP requests (24h)](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/http-requests-by-status.png)

## Tracing our Flask App
We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

[Jaeger traces](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger-trace.png)

## Jaeger in Dashboards
Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

[Jaeger service in Grafana](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger-datasource-dashboard.png)

## Report Error
Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name: Multiple requests returning HTTP 405 Method Not Allowed response

Date: 2021-11-10

Subject: Multiple requests returning HTTP 405 Method Not Allowed response

Affected Area: Back-end application

Severity: High

Description: Starting from today, after code update, we have noticed multiple requests being sent to /star method in 
back-end application returning HTTP 405 Method Not Allowed response. 
We have traced back the error to reference-app/backend/app.py file.


## Creating SLIs and SLOs
We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. 
Name four SLIs that you would use to measure the success of this SLO:
- Error rate: Error rate (number of 4xx and 5xx responses) in a month is 0.03% of all requests
- Uptime: Uptime of pods is 99.99% in a month
- Response rate & time: 99.97% of all requests respond in under 250ms
- Resources: CPU/Memory usage does not exceed the resources provided

## Building KPIs for our plan
Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

Error rate:
- Number of 4xx and 5xx HTTP request responses
- Number of requests on average
Those KPIs vere chosen to see all types of responses (as you later see in the dashboard - all in one graph) and to check 
if there is a correlation between average response time and response status code.

Uptime:
- Uptime of front-end application pods
- Uptime of back-end application pods
Seeing an indicator whether a pod is up or not is the clearest metric we can get. 
Used both for back-end and front-end applications.

Response rate & time:
- Average response time of requests
- Percentage of requests that returned responses under 250ms
Those metrics were chosen to check if the load of requests correlate to the response time.

Resources:
- Memory(RAM) usage for application pods
- CPU usage for application pods
When checking resources the main metrics to check are CPU and memory(RAM), because lacking those the application 
may get stuck or not run at all, especially when creating multiple pods.

## Final Dashboard
Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.

[Final dashboard](https://github.com/karolinasa/udacity-observability/tree/master/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/observability-dashboard.png)

The graphs created:
- Uptime of Pods: showing the status of front-end/back-end pods - green when up, red when down (by timestamp)
- No of requests/HTTP status: showing a number of requests in time grouped by request response including all types of responses (by timestamp)
- Average response time - All requests: requests grouped by pod and path and showing an average response time in 30s (by timestamp)
- Request rate under 250ms: showing a percentage of requests grouped by pod and path that had a response time under 250ms (by timestamp)
- Memory usage (Pods/default) - showing memory(RAM) usage for each pod in default namespace by timestamp (by timestamp)
- CPU usage (Pods/default) - showing CPU usage for each pod in default namespace (by timestamp)
