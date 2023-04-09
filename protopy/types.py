from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field

# TODO: Type narrow all of these Optional fields (could use @validator + Union)


class Session(BaseModel):
    did: str
    handle: str
    email: str
    accessJwt: str
    refreshJwt: str


class Viewer(BaseModel):
    muted: Optional[bool]
    following: Optional[str]


class Actor(BaseModel):
    did: str
    handle: str
    displayName: Optional[str]
    description: Optional[str]
    avatar: Optional[str]
    indexedAt: str
    viewer: Viewer


class Author(BaseModel):
    did: str
    handle: str
    displayName: Optional[str]
    avatar: Optional[str]
    viewer: Viewer


class RootId(BaseModel):
    cid: str
    uri: str


class ParentId(BaseModel):
    cid: str
    uri: str


class ReplyId(BaseModel):
    root: RootId
    parent: ParentId


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


class RecordImage(BaseModel):
    type: Literal["blob"] = Field(..., alias="$type")
    ref: RecordImageRef
    mimeType: Literal["image/jpeg"] | str  # TODO: This should only be valid image types
    size: int


class RecordImageData(BaseModel):
    alt: str
    image: RecordImage


class RecordImageEmbed(BaseModel):
    type: Literal["app.bsky.embed.images"] = Field(..., alias="$type")
    images: list[RecordImageData]


class Record(BaseModel):
    type: Literal["app.bsky.feed.post"] = Field(..., alias="$type")
    text: str
    createdAt: str  # datetime
    reply: Optional[ReplyId]
    facets: Optional[list[Facet]]
    embed: Optional[RecordImageEmbed]  # TODO: Add other types of embeds eg video


class Image(BaseModel):
    thumb: str
    fullsize: str
    alt: str


class Embed(BaseModel):
    type: Literal["app.bsky.embed.images#view"] = Field(..., alias="$type")
    images: list[Image]


class Post(BaseModel):
    uri: str
    cid: str
    author: Author
    record: Record
    replyCount: int
    repostCount: int
    likeCount: int
    indexedAt: str
    viewer: Viewer
    embed: Optional[Embed]


class Reply(BaseModel):
    root: Post
    parent: Post


class FeedItem(BaseModel):
    post: Post
    reply: Optional[Reply]


class Feed(BaseModel):
    feed: list[FeedItem]
    cursor: str


class Like(BaseModel):
    createdAt: str
    indexedAt: str
    actor: Actor


class Likes(BaseModel):
    uri: str
    cid: str
    cursor: str
    likes: list[Like]


class ThreadPost(BaseModel):
    type: Literal["app.bsky.feed.defs#threadViewPost"] = Field(..., alias="$type")
    post: Post
    parent: Optional[ThreadPost]
    replies: list[ThreadPost]


class Thread(BaseModel):
    thread: ThreadPost  # Recursive dict, not list
