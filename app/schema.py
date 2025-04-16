from pydantic import BaseModel, HttpUrl


class DetectRequest(BaseModel):
    url: HttpUrl
