import json
import os
from datetime import datetime
from config import DATA_PATH

# Plant database and seasonal data are loaded once at module load.
# This mirrors how a real service would cache its data source in memory.
with open(os.path.join(DATA_PATH, "plants.json"), encoding="utf-8") as f:
    _plant_db = json.load(f)

with open(os.path.join(DATA_PATH, "seasons.json"), encoding="utf-8") as f:
    _season_data = json.load(f)

# Maps calendar months to seasons for auto-detection.
_MONTH_TO_SEASON = {
    12: "winter", 1: "winter", 2: "winter",
    3: "spring", 4: "spring", 5: "spring",
    6: "summer", 7: "summer", 8: "summer",
    9: "fall",  10: "fall",  11: "fall",
}


def lookup_plant(plant_name: str) -> dict:
    """
    Search the plant database for a plant by name and return its care information.

    TODO — Milestone 1:

    Right now this always returns a "not found" response. Your job is to implement
    the search logic so it can actually find plants.

    The plant database (_plant_db) is a dict where keys are lowercase slugs like
    "pothos", "snake_plant", "fiddle_leaf_fig". Each plant also has a "display_name"
    field and an "aliases" list with common alternate names.

    Your implementation should handle all three:
      1. Direct key match (e.g., "pothos" → finds "pothos")
      2. Display name match (e.g., "Pothos" → finds "pothos")
      3. Alias match (e.g., "devil's ivy" → finds "pothos")

    All matching should be case-insensitive. Strip whitespace from the input.

    Return format when found:
      {"found": True, "plant": <the full plant dict>}

    Return format when not found:
      {"found": False, "name": <original input>, "message": <helpful string>}

    The message in the not-found case matters — the agent will use it to decide
    what to tell the user. Think about what would actually be helpful.

    Before writing code, complete specs/tool-functions-spec.md.
    """
    return {
        "found": False,
        "name": plant_name,
        "message": "Plant lookup not yet implemented. Complete Milestone 1.",
    }


def get_seasonal_conditions(season: str | None = None) -> dict:
    """
    Return current seasonal care context for houseplants.

    TODO — Milestone 1 (complete after lookup_plant):

    If `season` is provided (one of: "spring", "summer", "fall", "winter"),
    return the data for that season from _season_data.

    If `season` is None, auto-detect the current season based on the current
    calendar month. Use _MONTH_TO_SEASON for the mapping.

    Return the full season dict from _season_data, with one added field:
      "detected_season": True   — if season was auto-detected from the month
      "detected_season": False  — if season was passed as an argument

    Before writing code, complete specs/tool-functions-spec.md.
    """
    return {}
