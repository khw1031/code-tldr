from fastapi import APIRouter
from . import review

router = APIRouter()
router.include_router(review.router, prefix="/v1", tags=["Review"])
