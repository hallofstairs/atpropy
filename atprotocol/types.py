from pydantic import BaseModel


class Session(BaseModel):
    did: str
    handle: str
    email: str
    accessJwt: str
    refreshJwt: str
