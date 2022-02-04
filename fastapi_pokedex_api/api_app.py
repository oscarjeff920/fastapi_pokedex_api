from fastapi import FastAPI

from fastapi_pokedex_api import pokedex_schema
from fastapi_pokedex_api import pokeapi_requests
from fastapi_pokedex_api.configs.pokeapi_config import get_pokeapi_ip

app = FastAPI()


@app.get(
    "/pokedex/{poke_name}", response_model=pokedex_schema.PokedexBase, tags=["Pokemon"]
)
async def get_pokedata(poke_name: str) -> pokedex_schema.PokedexBase:
    return pokeapi_requests.get_pokedata(
        poke_name=poke_name, ip_settings=get_pokeapi_ip()
    )