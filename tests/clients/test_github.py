import pytest


@pytest.mark.asyncio
async def test_get(github_client, mocker, mock_response):
    resp = mock_response(200, {'foo': 'bar'})
    mocker.patch('aiohttp.ClientSession.get', return_value=resp)

    get_resp = await github_client._get('/some_url')
    assert get_resp == {'foo': 'bar'}


@pytest.mark.asyncio
async def test_get_commits(github_client, mocker, mock_response):
    resp = mock_response(200, commits_response)
    mocker.patch('aiohttp.ClientSession.get', return_value=resp)

    get_resp = await github_client.get_commits('login', 'repo')
    assert get_resp == [{
        'sha': c['sha'],
        'message': c['commit']['message'],
        'url': c['html_url']
    } for c in commits_response]

commits_response = [
    {
        "sha": "Second commit sha",
        "commit": {
            "message": "Second commit message"
        },
        "html_url": "Second commit url"
    },
    {
        "sha": "First commit sha",
        "commit": {
            "message": "First commit message"
        },
        "html_url": "First commit url"
    }
]
