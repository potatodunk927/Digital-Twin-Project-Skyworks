import csv, Recipe
recipes = []

with open("recptime_active_version.csv", 'utf-8') as file:
    reader = csv.DictReader()
    for row in reader:
        id = row["recpname"]
        process_time = (int(row["active_lower_bound"]) + int(row["active_lower_bound"])) / 2
        toolswap_time = 0
        recp = Recipe(id, process_time, toolswap_time)
        recipes.append(recp)
