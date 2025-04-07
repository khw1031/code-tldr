from atlassian.bitbucket import Cloud
from app.core.config import settings


def get_diff(repo_slug: str, pr_id: int):

    try:
        cloud = Cloud(
            cloud=True,
            token=settings.bitbucket_access_token,
        )

        workspace = cloud.workspaces.get(settings.bitbucket_workspace)
        repository = workspace.repositories.get(repo_slug)
        pull_request = repository.pullrequests.get(pr_id)
        diff = pull_request.diff()

        return diff

    except Exception as e:
        raise Exception(f"Error getting diff: {str(e)}")
