#!/usr/bin/env python3
from . import yt_search, prog_name
from urllib.parse import urlparse, quote

from . import prog_name

def interpret(aliases: dict[str, str], replace: str, replace2: str) -> str | None:
    alias_name = None
    return_me = None
    config = None
    if urlparse(replace).scheme in ("http", "https") and urlparse(replace).netloc:
        return_me = f"{replace}"
    elif replace.startswith("::"):
        # TODO: work on the parse
        alias_name = replace[2:]
        if aliases.get(alias_name) is None:
            raise KeyError(f"{prog_name}: the alias \'{alias_name}\' was not found!")
        else:
            return_me = f"{aliases.get(alias_name)}{replace2}"
    elif replace.startswith(":yt"):
        print(f"{prog_name}: querying yt-dlp...")
        if not replace2:
            raise ValueError(f"{prog_name}: not enough arguments")
        return_me = yt_search.find_vid(replace2, 0)
    else:
        raise ValueError(f"{prog_name}: {replace} is not a valid alias or URL!")
    if config:
        return_me = f"{return_me} -{config}"
    print(f"Your query returned: \'{return_me}\'")
    return return_me
    