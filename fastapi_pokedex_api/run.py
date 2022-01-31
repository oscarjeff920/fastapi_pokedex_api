import uvicorn

from fastapi_pokedex_api.configs.pokedex_api_config import get_api_config
from fastapi_pokedex_api.pokeapi_requests import app

if __name__ == "__main__":
    api_settings = get_api_config()
    uvicorn.run(
        app, host=api_settings.POKEDEX_API_HOST, port=api_settings.POKEDEX_API_PORT
    )
