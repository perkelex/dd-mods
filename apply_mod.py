import argparse
import configparser
import shutil
from pathlib import Path

argparser = argparse.ArgumentParser(
    prog="apply",
    description="Applies mod to DarkestDungeon installation configured in mods.ini"
)

argparser.add_argument("mod_name")
args = argparser.parse_args()

config = configparser.ConfigParser()
config.read("mods.ini")

src = Path(f"./{args.mod_name}").absolute()
dst = Path(config["GAME"]["Location"])

shutil.copytree(src, dst, dirs_exist_ok=True)