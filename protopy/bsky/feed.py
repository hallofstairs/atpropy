# %% Imports
import requests

from protopy.types import Feed, Likes, Session, Thread

# TODO: Add checks for parameters, eg acceptable `limit` range
# TODO: Add docstrings


def get_author_feed(host: str, session: Session, actor: str, limit: int) -> Feed:
    """A view of an actor's feed."""

    return Feed.parse_obj(
        requests.get(
            f"{host}/xrpc/app.bsky.feed.getAuthorFeed?actor={actor}&limit={limit}",
            headers={"Authorization": f"Bearer {session.accessJwt}"},
        ).json()
    )


def get_timeline(host: str, session: Session) -> Feed:
    """A view of the user's home timeline."""

    return Feed.parse_obj(
        requests.get(
            f"{host}/xrpc/app.bsky.feed.getTimeline",
            headers={"Authorization": f"Bearer {session.accessJwt}"},
        ).json()
    )


def get_likes(host: str, session: Session, uri: str, cid: str, limit: int) -> Likes:
    """A view of a post's likes."""

    return Likes.parse_obj(
        requests.get(
            f"{host}/xrpc/app.bsky.feed.getLikes?uri={uri}&cid={cid}&limit={limit}",
            headers={"Authorization": f"Bearer {session.accessJwt}"},
        )
    )


def get_post_thread(host: str, session: Session, uri: str, depth: int) -> Thread:
    """A view of a post's related threads."""

    return Thread.parse_obj(
        requests.get(
            f"{host}/xrpc/app.bsky.feed.getPostThread?uri={uri}&depth={depth}",
            headers={"Authorization": f"Bearer {session.accessJwt}"},
        )
    )
