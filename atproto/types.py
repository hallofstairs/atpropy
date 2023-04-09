from typing import Optional

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
    pass


class Author(BaseModel):
    did: str
    handle: str
    displayName: str
    avatar: str
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


class Feature(BaseModel):
    did: str
    type_field: str = Field(..., alias="$type")


class Facet(BaseModel):
    type_field: str = Field(..., alias="$type")
    index: Index
    features: list[Feature]


class Record(BaseModel):
    text: str
    type_field: str = Field(..., alias="$type")
    createdAt: str  # datetime
    reply: Optional[ReplyId]
    facets: Optional[list[Facet]]


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


class Reply(BaseModel):
    root: Post
    parent: Post


class FeedItem(BaseModel):
    post: Post
    reply: Optional[Reply]


class Feed(BaseModel):
    feed: list[FeedItem]
    cursor: str
