from atlassian.bitbucket import Cloud


async def get_diff(repo_slug: str, pr_id: int, access_token: str, workspace: str):
    workspace = Cloud(username=None, password=None, cloud=True, token=access_token)

    try:
        bitbucket = Cloud(username="", password="", cloud=True)
        diff = bitbucket.repositories.pullrequests.diff(
            workspace=workspace, repository_slug=repo_slug, pull_request_id=pr_id
        )
        return diff
    except Exception as e:
        raise Exception(f"Error getting diff: {str(e)}")
