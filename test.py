from tools import lookup_plant, get_seasonal_conditions

# Fetch and print the details for Devil's Ivy
# (We use double quotes here so the apostrophe in "devil's" doesn't break the string)
plant_info = lookup_plant("devil's ivy")
print(plant_info)

# Fetch and print the current seasonal conditions
conditions = get_seasonal_conditions()
print(conditions)