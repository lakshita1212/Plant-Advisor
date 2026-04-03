# Spec: Tool Functions

**File:** `tools.py`
**Status:** Spec incomplete — fill in all blank fields before implementing

---

## Purpose

These two functions are the tools the agent can call. They retrieve structured data from the local plant database and seasonal data files and return it to the agent loop, which passes it to the LLM as context for generating a response.

---

## Function 1: `lookup_plant()`

### Input / Output Contract

**Inputs:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `plant_name` | `str` | The plant name as entered by the user or chosen by the LLM — may be any casing, common name, scientific name, or alias |

**Output:** `dict`

When the plant is **found**, return:
```python
{"found": True, "plant": <the full plant dict from _plant_db>}
```

When the plant is **not found**, return:
```python
{"found": False, "name": <normalized input>, "message": <helpful string>}
```

---

### Design Decisions

*Complete these fields before writing code. Use Plan or Ask mode to think through what belongs in each field.*

---

#### Input normalization

*How will you normalize the plant_name input before searching? What transformations are needed?*

```
[your answer here]
```

---

#### Search order

*The database has three ways a plant can be identified: its key (e.g., "pothos"), its display_name (e.g., "Pothos"), and its aliases list (e.g., ["golden pothos", "devil's ivy"]). What order will you search these, and why?*

```
[your answer here]
```

---

#### Alias matching approach

*Aliases are stored as a list of strings. How will you check if the input matches any alias?*

```
[your answer here]
```

---

#### Not-found message

*Write the exact message string you'll return when a plant isn't found. What information makes it actually helpful to the agent?*

```
[your answer here]
```

---

#### Implementation Notes

*Fill this in after implementing.*

**Test: does `"devil's ivy"` return the pothos entry?**
```
[yes / no — if no, describe what happened]
```

**Test: does `"SNAKE PLANT"` return the snake plant entry?**
```
[yes / no — if no, describe what happened]
```

**One edge case you discovered while implementing:**
```
[your answer here]
```

---

## Function 2: `get_seasonal_conditions()`

### Input / Output Contract

**Inputs:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `season` | `str \| None` | One of `"spring"`, `"summer"`, `"fall"`, `"winter"`, or `None` to auto-detect |

**Output:** `dict`

The full season dict from `_season_data`, plus one additional field:

| Added field | Type | Value |
|-------------|------|-------|
| `"detected_season"` | `bool` | `True` if auto-detected from the month; `False` if season was passed as an argument |

---

### Design Decisions

*Complete these fields before writing code.*

---

#### Auto-detection logic

*Describe how you will determine the current season when `season` is `None`. What data source will you use?*

```
[your answer here]
```

---

#### Season validation

*What happens if a caller passes an invalid season string (e.g., `"monsoon"`)? How will you handle it?*

```
[your answer here]
```

---

#### Return structure

*Sketch out what a complete return value looks like — pick any season as an example.*

```
[your answer here]
```

---

#### Implementation Notes

*Fill this in after implementing.*

**Test: does calling with `season=None` return the correct season for the current month?**
```
Current month: [month]
Expected season: [season]
Returned season: [season]
```

**Test: does calling with `season="winter"` return winter data regardless of the current month?**
```
[yes / no]
```
