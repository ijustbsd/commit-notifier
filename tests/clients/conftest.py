import aiohttp
import pytest
from app.clients import GithubClient


class MockResponse:
    def __init__(self, status, json):
        self.status = status
        self._json = json

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def json(self):
        return self._json


@pytest.fixture
async def session():
    return aiohttp.ClientSession()


@pytest.fixture
def github_client(session):
    return GithubClient(session, "token")


@pytest.fixture
def mock_response():
    return MockResponse
