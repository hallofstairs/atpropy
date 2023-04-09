import requests

from atproto.types import Feed, Session


def get_author_feed(host: str, session: Session, handle: str, limit: int) -> Feed:
    headers = {"Authorization": f"Bearer {session.accessJwt}"}
    resp = requests.get(
        f"{host}/xrpc/app.bsky.feed.getAuthorFeed?actor={handle}&limit={limit}",
        headers=headers,
    )
    return Feed.parse_obj(resp.json())
