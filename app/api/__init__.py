from fastapi import APIRouter
from . import v1

router = APIRouter()
router.include_router(v1.router, prefix="/api", tags=["v1"])
