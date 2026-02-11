import json
from pathlib import Path

INDEX_PATH = "/home/krft/.local/share/PrismLauncher/assets/indexes/1.16.json"
OBJECTS_PATH = "/home/krft/.local/share/PrismLauncher/assets/objects/"
OUTPUT_PATH = "./langfiles/"

hashes = []

with open(INDEX_PATH) as file:
    index = json.load(file)
objects = index["objects"]

for objname in objects:
    if not objname.startswith("minecraft/lang/"):
        continue
    hash = objects[objname]["hash"]
    dirname = hash[:2]
    langpath: Path = OBJECTS_PATH / Path(dirname) / hash
    newpath = langpath.copy_into(OUTPUT_PATH)
    langname = objname.split("/")[-1]
    newpath.rename(newpath.parent / langname)
