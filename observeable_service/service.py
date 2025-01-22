from prometheus_client import Counter, generate_latest
from fastapi.responses import PlainTextResponse

request_counter = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'status_code', 'response_time'])

class MetricsService:
    def __init__(self):
        pass

    def get_metrics(self):
        return PlainTextResponse(content=generate_latest(), media_type="text/plain", status_code=200)