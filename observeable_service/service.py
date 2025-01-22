from prometheus_client import Counter

request_counter = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'status_code', 'response_time'])