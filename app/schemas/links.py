from pydantic import BaseModel, HttpUrl


class LinkBase(BaseModel):
    url: HttpUrl


class LinkCreate(LinkBase):
    pass


class LinkUpdate(LinkBase):
    pass


class LinkRead(LinkBase):
    id: str
    hash_key: str
