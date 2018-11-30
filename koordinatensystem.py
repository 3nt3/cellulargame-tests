import json
import matplotlib.pyplot as plt
import requests


r = requests.get("http://localhost:8000/spawnFood")

data = []
coords = [[], []]
colors = []

data = json.loads(r.text)
for item in data:
	coords[0].append(item["pos"][0])
	coords[1].append(item["pos"][1])
	print(item["value"])
	if item["value"] == 5:
		colors.append("r")
	elif item["value"] == 10:
		colors.append("g")
	else:
		colors.append("b")


days = list(range(1,9))
x = [4, 1]
y = [3, 5]
plt.scatter(coords[0], coords[1], c=colors)
plt.show()
