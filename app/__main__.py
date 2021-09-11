import asyncio
import logging

import aiohttp

from .clients import GithubClient, TelegramBotClient
from .config import settings
from .database import manager as db_manager
from .database import models, utils

logger = logging.getLogger("main")

utils.create_tables()


async def handle_commits(gh_client, tg_bot_client):
    persons = await db_manager.execute(models.Person.select())
    for person in persons:
        commits = await gh_client.get_commits(
            person.github_username,
            person.github_repo,
        )
        commits = commits[::-1]

        if not commits:
            return

        exist_commits = [commit.sha for commit in person.commits]
        new_commits = [c for c in commits if c["sha"] not in exist_commits]

        if not new_commits:
            return

        for commit in new_commits:
            await db_manager.create(
                models.Commit,
                author=person,
                sha=commit["sha"],
            )

        commits_text = "\n".join(
            [
                f"{n}. [{c['message']}]({c['url']})"
                for n, c in enumerate(new_commits, 1)
            ],
        )

        message = f"*{person.full_name}*:\n" + commits_text

        await tg_bot_client.send_message(
            message,
            settings.TG_CHAT_ID,
            {
                "parse_mode": "Markdown",
                "disable_web_page_preview": "True",
            },
        )


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GithubClient(session, settings.GITHUB_TOKEN)
        tg_bot = TelegramBotClient(session, settings.TG_BOT_TOKEN)

        await handle_commits(gh, tg_bot)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_until_complete(db_manager.close())
