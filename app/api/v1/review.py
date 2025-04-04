from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from app.schemas.review import Review

router = APIRouter()


@router.post("/review")
async def get_review(payload: Review):
    comment = payload.comment.content.raw

    if "@ssem" not in comment:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    # 여기에 @ssem이 포함된 경우의 로직 구현
    return JSONResponse(
        content={"status": "processing", "message": "Review request received"},
        status_code=status.HTTP_200_OK,
    )
