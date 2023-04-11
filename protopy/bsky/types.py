from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field


class Viewer(BaseModel):
    muted: Optional[bool]
    following: Optional[str]


class Actor(BaseModel):
    """A reference to an actor in the network."""

    did: str
    handle: str
    displayName: Optional[str]
    description: Optional[str]
    avatar: Optional[str]
    indexedAt: Optional[str]
    viewer: Viewer


class Profile(Actor):
    banner: Optional[str]
    followsCount: int
    followersCount: int
    postsCount: int


class Profiles(BaseModel):
    profiles: list[Profile]


class Author(BaseModel):
    did: str
    handle: str
    displayName: Optional[str]
    avatar: Optional[str]
    viewer: Viewer


class PostId(BaseModel):
    cid: str
    uri: str


class ReplyId(BaseModel):
    root: PostId
    parent: PostId


class Index(BaseModel):
    byteEnd: int
    byteStart: int


class MentionFeature(BaseModel):
    type: Literal["app.bsky.richtext.facet#mention"] = Field(..., alias="$type")
    did: str


class LinkFeature(BaseModel):
    type: Literal["app.bsky.richtext.facet#link"] = Field(..., alias="$type")


class Facet(BaseModel):
    type: Optional[Literal["app.bsky.richtext.facet"]] = Field(None, alias="$type")
    index: Index
    features: list[MentionFeature | LinkFeature]


class RecordImageRef(BaseModel):
    link: str = Field(..., alias="$link")


class Thumbnail(BaseModel):
    type: Literal["blob"] = Field(..., alias="$type")
    ref: RecordImageRef
    mimeType: Literal["image/jpeg"] | str  # TODO: This should only be valid image types
    size: int


class RecordImageData(BaseModel):
    alt: str
    image: Thumbnail


class RecordImageEmbed(BaseModel):
    type: Literal["app.bsky.embed.images"] = Field(..., alias="$type")
    images: list[RecordImageData]


class RecordExternalData(BaseModel):
    uri: str
    thumb: Thumbnail
    title: str
    description: str


class RecordExternalEmbed(BaseModel):
    type: Literal["app.bsky.embed.external"] = Field(..., alias="$type")
    external: RecordExternalData


class Record(BaseModel):
    type: Literal["app.bsky.feed.post"] = Field(..., alias="$type")
    text: str
    createdAt: str  # datetime
    reply: Optional[ReplyId]
    facets: Optional[list[Facet]]
    embed: Optional[
        RecordImageEmbed | RecordExternalEmbed
    ]  # TODO: Add other types of embeds


class Image(BaseModel):
    thumb: str
    fullsize: str
    alt: str


class ImageEmbed(BaseModel):
    type: Literal["app.bsky.embed.images#view"] = Field(..., alias="$type")
    images: list[Image]


class External(BaseModel):
    uri: str
    title: str
    description: str
    thumb: str


class ExternalEmbed(BaseModel):
    type: Literal["app.bsky.embed.external#view"] = Field(..., alias="$type")
    external: External


class Post(PostId):
    author: Author
    record: Record
    replyCount: int
    repostCount: int
    likeCount: int
    indexedAt: str
    viewer: Viewer
    embed: Optional[ExternalEmbed | ImageEmbed]


class Reply(BaseModel):
    root: Post
    parent: Post


class FeedItem(BaseModel):
    post: Post
    reply: Optional[Reply]


class Feed(BaseModel):
    feed: list[FeedItem]
    cursor: Optional[str]


class Like(BaseModel):
    createdAt: str
    indexedAt: str
    actor: Actor


class Likes(PostId):
    cursor: Optional[str]
    likes: list[Like]


class Reposts(PostId):
    cursor: Optional[str]
    repostedBy: list[Actor]


class ThreadPost(BaseModel):
    type: Literal["app.bsky.feed.defs#threadViewPost"] = Field(..., alias="$type")
    post: Post
    parent: Optional[ThreadPost]
    replies: list[ThreadPost]


class Thread(BaseModel):
    thread: ThreadPost


class ActorResults(BaseModel):
    cursor: Optional[str]
    actors: list[Actor]


class Followers(BaseModel):
    subject: Actor
    followers: list[Actor]
