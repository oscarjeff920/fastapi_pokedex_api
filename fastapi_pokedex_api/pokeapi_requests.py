import fastapi
import pydantic.error_wrappers
import requests
from pydantic import typing

from fastapi_pokedex_api.configs.pokeapi_config import PokeapiSettings
from fastapi_pokedex_api.pokedex_schema import PokedexBase


def get_pokedata(ip_settings: PokeapiSettings, poke_name: str) -> PokedexBase:
    name = poke_name.lower()
    try:
        response = requests.get("{}{}".format(ip_settings.POKEAPI_IP, name))
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        raise fastapi.HTTPException(
            status_code=404,
            detail="pokemon '{}' not found. Check spelling".format(name),
        )

    try:
        details = response.json()
    except requests.exceptions.JSONDecodeError:
        raise fastapi.HTTPException(status_code=406, detail="response not jsonable")

    try:
        return PokedexBase(
            name=name,
            description=english_description(details.get("flavor_text_entries", {})),
            habitat=details.get("habitat").get("name")
            if details.get("habitat") is not None
            else None,
            is_legendary=details.get("is_legendary"),
        )
    except pydantic.error_wrappers.ValidationError:
        raise fastapi.HTTPException(
            status_code=406, detail="received json does not have required keys"
        )


def english_description(descriptions: typing.List) -> typing.Optional[str]:
    for entry in descriptions:
        if entry.get("language").get("name") == "en":
            return entry.get("flavor_text").replace("\n", " ").replace("\u000c", " ")
    else:
        return None
