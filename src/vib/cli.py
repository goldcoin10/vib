#!/usr/bin/env python3
import shlex
import shutil
import subprocess
import sys
import os
from pathlib import Path
from . import prog_name, interpreter
from importlib.metadata import version

def main():
    vibrc: str = f"{str(Path.home())}/.vibrc"
    arg: str | None = None
    arg2: str | None = None
    if not len(sys.argv) < 3:
        arg2 = sys.argv[2]
    if not len(sys.argv) < 2:
        arg = sys.argv[1]
    else:
        print(f"{prog_name}: No arguments given.")
        sys.exit()
    if not shutil.which("surf"):
            raise FileNotFoundError(f"{prog_name}: Surf is not on your system!")
    if arg == "--check-surf":
            print(f"{prog_name}: Surf is installed on your system.")
    elif arg == "--def-rc":
        Path(vibrc).touch()
        file = open(vibrc, "w")
        file.write('# this is a Vib config file\n# (:a for alias, :c for config)\n:a "https://wikipedia.org/" wiki\n')
        file.close()
    elif arg == "--help":
        print(f"vib {version("vib")}")
        print("\t--help : prints this help message")
        print("\t--check-surf : checks if the surf browser is in your PATH")
        print("\t--def-rc : overrides your .vibrc to defaults")
        print("\t:yt : prints the URL of the title inserted")
        print("\tcheck your .vibrc (located at ~/.vibrc) for more details")
    else:
        print(f"{prog_name}: reading .vibrc... ({vibrc})")
        if os.path.isfile(vibrc):
            f = open(vibrc, "rt")
            config: list[str] = [
                line for line in f.read().splitlines()
                if line.strip() and not line.lstrip().startswith("#")
            ]
            alias_dict = {}
            config_dict = {} # TODO: attach this to :c
            for line in config:
                parts = shlex.split(line)
                if len(parts) == 3 and parts[0] == ":a":
                    alias_dict[parts[2]] = parts[1]
                elif len(parts) == 3 and parts[0] == ":c":
                    config_dict[parts[2]] = parts[1]
                else:
                    raise SyntaxError()
            f.close()
        else:
            print(f"{prog_name}: {vibrc} is not found, create with \'vib --def-rc\'")
            sys.exit(1)
        if arg.startswith("::"):
            if arg2 is None:
                print(f"{prog_name}: there is no second parameter to the alias")
                sys.exit(1)
        parms_to_browser = interpreter.interpret(alias_dict, arg, arg2)
        subprocess.run(["surf", parms_to_browser])
        print()


if __name__ == "__main__":
    sys.exit(main())