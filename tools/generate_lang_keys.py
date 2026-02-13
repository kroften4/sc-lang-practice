import json
from pathlib import Path

LANG_PATH = "/home/krft/github/sc-lang-practice/static/langfiles/en_gb.json"
OUTPUT_PATH = "./lang_keys.json"

with open(LANG_PATH) as file:
    langfile = json.load(file)

with open(OUTPUT_PATH, "w") as file:
    out = list(langfile.keys())
    json.dump(out, file)
