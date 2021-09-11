class TelegramBotClient:
    def __init__(self, session, token) -> None:
        self.session = session

        self.base_url = f"https://api.telegram.org/bot{token}"

    async def _get(self, endpoint, params) -> None:
        url = self.base_url + endpoint
        await self.session.get(url, params=params)

    async def send_message(self, text, chat_id, params=None) -> None:
        if params is None:
            params = {}
        get_params = {
            "chat_id": chat_id,
            "text": text,
            **params,
        }
        await self._get("/sendMessage", get_params)
