import requests

from protopy.types import Session

# class Session:
#     def __init__(self, host: str, username: str, password: str) -> None:
#         self.host = host
#         self.username = username
#         self.password = password


def create_session(host: str, username: str, password: str) -> Session:
    resp = requests.post(
        f"{host}/xrpc/com.atproto.server.createSession",
        json={"identifier": username, "password": password},
    )
    return Session.parse_obj(resp.json())
