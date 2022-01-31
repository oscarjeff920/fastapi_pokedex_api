from pydantic import BaseModel, typing


class PokedexBase(BaseModel):
    name: str
    description: str
    habitat: typing.Optional[str]
    is_legendary: bool
