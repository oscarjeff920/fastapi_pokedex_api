from fastapi import FastAPI

from fastapi_pokedex_api import pokedex_schema, pokeapi_requests

app = FastAPI()


@app.get(
    "/pokedex/{poke_name}", response_model=pokedex_schema.PokedexBase, tags=["Pokemon"]
)
async def get_pokedata(poke_name: str) -> pokedex_schema.PokedexBase:
    return pokeapi_requests.get_pokedata(poke_name=poke_name)
