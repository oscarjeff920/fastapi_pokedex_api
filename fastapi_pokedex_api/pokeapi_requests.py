import fastapi
import requests
from pydantic import typing

from fastapi_pokedex_api.configs.pokeapi_config import get_pokeapi_ip
from fastapi_pokedex_api.pokedex_schema import PokedexBase


def get_pokedata(poke_name: str) -> PokedexBase:
    ip = get_pokeapi_ip().POKEAPI_IP
    name = poke_name.lower()
    try:
        response = requests.get("{}{}".format(ip, name))
        response.raise_for_status()
    except fastapi.HTTPException as httperr:
        raise httperr

    details = response.json()
    return PokedexBase(
        name=name,
        description=english_description(details.get("flavor_text_entries", {})),
        habitat=details.get("habitat").get("name")
        if details.get("habitat") is not None
        else None,
        is_legendary=details.get("is_legendary"),
    )


def english_description(descriptions: typing.List) -> typing.Optional[str]:
    for entry in descriptions:
        if entry.get("language").get("name") == "en":
            return entry.get("flavor_text").replace("\n", " ").replace("\u000c", " ")
    else:
        return None
