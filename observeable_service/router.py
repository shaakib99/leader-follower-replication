from fastapi import APIRouter
from observeable_service.service import MetricsService

router = APIRouter(prefix="/metrics", tags=["Metrics"])

metrics_service = MetricsService()

@router.get("/")
async def get_metrics():
    return metrics_service.get_metrics()