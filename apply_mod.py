import argparse
import configparser
import shutil
from pathlib import Path

exclusions = [".venv", ".git"]

argparser = argparse.ArgumentParser(
    prog="apply",
    description="Applies mod to DarkestDungeon installation configured in mods.ini"
)

argparser.add_argument("--one", dest="one_mod_name", default=None, required=False)
argparser.add_argument("all")
args = argparser.parse_args()

config = configparser.ConfigParser()
config.read("mods.ini")

dst = Path(config["GAME"]["Location"]).absolute()

if (args.one_mod_name):
    shutil.copytree(Path(args.one_mod_name).absolute(), dst, dirs_exist_ok=True)
elif(args.all):
    for mod in [file for file in Path(".").glob('*') if file.is_dir() and file.stem not in exclusions]:
        shutil.copytree(mod.absolute(), dst, dirs_exist_ok=True)
