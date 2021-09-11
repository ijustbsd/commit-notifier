import typing as t


class GithubClient:
    def __init__(self, session, token) -> None:
        self.session = session
        self.headers = {
            "Authorization": f"token {token}",
        }

    async def _get(self, url) -> t.Any:
        async with self.session.get(url, headers=self.headers) as resp:
            if resp.status != 200:
                return None
            return await resp.json()

    async def get_commits(self, login, repo_name) -> t.List[t.Dict]:
        data = await self._get(
            f"https://api.github.com/repos/{login}/{repo_name}/commits",
        )
        if data is None:
            return []
        return [
            {
                "sha": commit["sha"],
                "message": commit["commit"]["message"],
                "url": commit["html_url"],
            }
            for commit in data
        ]
