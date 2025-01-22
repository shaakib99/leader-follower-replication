from pydantic import BaseModel

class RequestModel(BaseModel):
    url: str
    method: str
    status_code: int
    response_time: float