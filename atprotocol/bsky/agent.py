import requests

from atprotocol import AtpAgent
from atprotocol.bsky.types import (
    ActorResults,
    Feed,
    Followers,
    Likes,
    Profile,
    Profiles,
    Reposts,
    Thread,
)

BSKY_SERVICE_URL = "https://bsky.social:443"
BSKY_DEFAULT_LIMIT = 50


class BskyAgent(AtpAgent):
    """Agent for interacting with the Bluesky app."""

    def __init__(self, service: str = BSKY_SERVICE_URL) -> None:
        super().__init__(service)

    def get_timeline(self) -> Feed:
        """A view of your home timeline."""

        return Feed.parse_obj(
            requests.get(
                url=f"{self.service}/xrpc/app.bsky.feed.getTimeline",
                headers=self._get_auth_header(),
            ).json()
        )

    def get_author_feed(self, actor: str, limit: int = BSKY_DEFAULT_LIMIT) -> Feed:
        """A view of an actor's feed."""

        return Feed.parse_obj(
            requests.get(
                url=f"{self.service}/xrpc/app.bsky.feed.getAuthorFeed?actor={actor}&limit={limit}",
                headers=self._get_auth_header(),
            ).json()
        )

    def get_post_thread(self, uri: str, depth: int) -> Thread:
        """A view of a post's related threads."""

        return Thread.parse_obj(
            requests.get(
                url=f"{self.service}/xrpc/app.bsky.feed.getPostThread?uri={uri}&depth={depth}",
                headers=self._get_auth_header(),
            ).json()
        )

    def get_likes(self, uri: str, cid: str, limit: int = BSKY_DEFAULT_LIMIT) -> Likes:
        """A view of a post's likes."""

        return Likes.parse_obj(
            requests.get(
                url=f"{self.service}/xrpc/app.bsky.feed.getLikes?uri={uri}&cid={cid}&limit={limit}",
                headers=self._get_auth_header(),
            ).json()
        )

    def get_reposted_by(
        self, uri: str, cid: str, limit: int = BSKY_DEFAULT_LIMIT
    ) -> Reposts:
        """A view of a post's reposts."""

        return Reposts.parse_obj(
            requests.get(
                url=f"{self.service}/xrpc/app.bsky.feed.getRepostedBy?uri={uri}&cid={cid}&limit={limit}",
                headers=self._get_auth_header(),
            ).json()
        )

    def get_followers(self, actor: str):
        """Who is following an actor?"""

        return Followers.parse_obj(
            requests.get(
                url=f"{self.service}/xrpc/app.bsky.graph.getFollowers?actor={actor}",
                headers=self._get_auth_header(),
            ).json()
        )

    def get_profile(self, actor: str) -> Profile:
        """Get the profile for an actor."""

        return Profile.parse_obj(
            requests.get(
                url=f"{self.service}/xrpc/app.bsky.actor.getProfile?actor={actor}",
                headers=self._get_auth_header(),
            ).json()
        )

    def get_profiles(self, actors: list[str]):
        """Get the profiles for a list of actors."""

        return Profiles.parse_obj(
            requests.get(
                url=(
                    f"{self.service}/xrpc/app.bsky.actor.getProfiles?"
                    + "".join([f"actors={actor}&" for actor in actors])
                ),
                headers=self._get_auth_header(),
            ).json()
        )

    def search_actors(self, term: str, limit: int = BSKY_DEFAULT_LIMIT):
        """Find actors matching search criteria."""

        return ActorResults.parse_obj(
            requests.get(
                url=f"{self.service}/xrpc/app.bsky.actor.searchActors?term={term}&limit={limit}",
                headers=self._get_auth_header(),
            ).json()
        )
