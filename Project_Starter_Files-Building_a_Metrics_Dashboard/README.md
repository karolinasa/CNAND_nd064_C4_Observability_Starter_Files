**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

Run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

Pods: 

[Namespace: default](Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/pods-default.png) 

[Namespace: monitoring](Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/pods-monitoring.png) 

[Namespace: observability](Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/pods-observability.png)

Services: 

[All services](Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/services.png)

## Setup the Jaeger and Prometheus source
Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

[Grafana homepage](Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana-homepage.png)

## Create a Basic Dashboard
Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

To create a dashboard I used a reference dashboard in the [project repository](Project_Starter_Files-Building_a_Metrics_Dashboard/reference-dashboards/kubernetes-cluster-monitoring-via-prometheus_rev3.json).

[Basic Grafana Dashboard with Prometheus as a source](Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/prometheus-datasource-reference-dashboard.png)

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

[Uptime (1h)](Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/uptime.png) 

[HTTP requests (24h)](Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/http-requests-by-status.png)

## Tracing our Flask App
We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

[Jaeger traces](Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger-trace.png)

## Jaeger in Dashboards
Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.
[Jaeger service in Grafana](Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger-datasource-dashboard.png)

## Report Error
Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

## Final Dashboard
Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

[Final dashboard](Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/observability-dashboard.png)
