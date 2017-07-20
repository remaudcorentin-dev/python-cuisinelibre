
from cuisinelibre import CuisineLibre

# Search :
query_options = {
  "recherche": "banane",     # Query
  "lang": "fr", 	   # Recipies Language
}
query_result = CuisineLibre.search(query_options)

for result in query_result:
	print("## %s" % result["name"])

	data = CuisineLibre.get(result["url"])
	print(data["ingredients_title"])
	for ingr in data["ingredients"]:
		print(" - %s" % (ingr))
	print("--")
	for instr in data["instructions"]:
		print("%s\n" % instr)

	print("\n\n")
