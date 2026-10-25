#!/usr/bin/env python3
from . import yt_search, prog_name
from urllib.parse import urlparse, quote

from . import prog_name

def interpret(aliases: dict[str, str], replace: str, replace2: str, config_list: dict[str, str]) -> list[str] | None:
    alias_name = None
    return_me = [None]*2
    config = None
    if urlparse(replace).scheme in ("http", "https") and urlparse(replace).netloc:
        return_me[0] = f"{replace}"
    elif replace.startswith("::"):
        # TODO: work on the parse
        alias_name = replace[2:]
        if aliases.get(alias_name) is None:
            raise KeyError(f"{prog_name}: the alias \'{alias_name}\' was not found!")
        else:
            return_me[0] = f"{aliases.get(alias_name)}{replace2}"
    elif replace.startswith(":yt"):
        print(f"{prog_name}: querying yt-dlp...")
        yt_data = yt_search.find_vid(replace2)
        print(f"Your query returned: {yt_data[1]}")
        if not replace2:
            raise ValueError(f"{prog_name}: not enough arguments")
        return_me[0] = yt_data[0]
    else:
        raise ValueError(f"{prog_name}: {replace} is not a valid alias or URL!")
    for key, value in config_list.items():
        value = value == "True"
        if key == "CookiesDisabled" and value is True:
            config = f"-a a@A "
        elif key == "CookiesDisabled" and value is False:
            config = f"{config}-a A@a "
        elif key == "Fullscreen" and value is True:
            config = f"{config}-F"
        elif key == "Fullscreen" and value is False:
            config = f"{config}-f"
        else:
            print(config_list)
            raise ValueError(f"{prog_name}: the configuration token \'{key}\' is invalid!")
    if config:
        return_me[1] = config
    return return_me
    