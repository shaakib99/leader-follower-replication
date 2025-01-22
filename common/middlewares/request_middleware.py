from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse, Response
from datetime import datetime
from observeable_service.service import request_counter

class RequestMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, excluded_endpoints: list[str] = []):
        super().__init__(app)
        self.excluded_endpoints = excluded_endpoints

    async def dispatch(self, request: Request, call_next):
        if request.url.path in self.excluded_endpoints:
            return await call_next(request)
        
        start_time = datetime.now()
        try:
            response = await call_next(request)
            body = b"".join([chunk async for chunk in response.body_iterator])

            request_counter.labels(method= request.method, endpoint= request.url.path, status_code= response.status_code, response_time= (datetime.now() - start_time).total_seconds()).inc()
            return Response(status_code=response.status_code, content=body, headers=dict(response.headers), media_type=response.media_type)
        except Exception as e:
            request_counter.labels(method= request.method, endpoint= request.url.path, status_code= 500, response_time= (datetime.now() - start_time).total_seconds()).inc()
            return JSONResponse(status_code=500, content={"message": e.__str__()})