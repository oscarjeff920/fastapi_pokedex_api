from fastapi import FastAPI

from fastapi_pokedex_api import pokedex_schema
from fastapi_pokedex_api import api_app

app = FastAPI()


@app.get(
    "/pokedex/{poke_name}", response_model=pokedex_schema.PokedexBase, tags=["Pokemon"]
)
async def get_pokedata(poke_name: str) -> pokedex_schema.PokedexBase:
    return api_app.get_pokedata(poke_name=poke_name)
