from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from app.schemas import Review
from app.services.diff import get_diff

router = APIRouter()


@router.post("/review")
async def get_review(payload: Review):
    comment = payload.comment.content.raw

    if "@ssem" not in comment:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    repo_slug = payload.repository.name
    pr_id = payload.pull_request.id
    # pr_title = payload.pull_request.title
    # pr_description = payload.pull_request.description

    diff = get_diff(repo_slug, pr_id)
    # print(diff)
    return JSONResponse(
        content={"status": "processing", "message": "Review request received"},
        status_code=status.HTTP_200_OK,
    )
