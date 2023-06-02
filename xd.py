import coverpy
import requests

# Instance CoverPy
coverpy = coverpy.CoverPy()
# Set a limit. There is a default (1), but I set it manually to showcase usage.
limit = 1

try:
	result = coverpy.get_cover("Turn It Up - Single Armin van Buuren", limit)
	# Set a size for the artwork (first parameter) and get the result url.
	print(result.name)
	print(result.artwork(100))
except requests.exceptions.HTTPError:
	print("Could not execute GET request")
except Exception as e:
	print("Nothing found.")