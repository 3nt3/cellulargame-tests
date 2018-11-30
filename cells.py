import json
import matplotlib.pyplot as plt
import requests
import random

coords = [[], []]
sizes = []
colors = []
lbls = []
relCoords = []


r = requests.get("http://localhost:8000/delall")

fig = plt.subplot()

for i in range(10):
	name = f"der echte {i}"
	r = requests.post("http://localhost:8000/initCell", json.dumps(name))
	r = requests.post(f"http://localhost:8000/updateSize/{i}", str(random.randint(10, 100)))
	print(r.text)

	if i == 5:
		colors.append("#2ecc71")
	else:
		colors.append("#3498db")
	#print(int(r.text))

r = requests.get("http://localhost:8000/getCells")
data = json.loads(r.text)

for item in data:
	print(item)
	coords[0].append(item["Pos"][0])
	coords[1].append(item["Pos"][1])
	sizes.append(item["Size"]*10)
	fig.annotate(str((coords[0][-1], coords[1][-1])), (coords[0][-1], coords[1][-1]))


r = requests.get("http://localhost:8000/spawnFood")
foodData = json.loads(r.text)

for food in foodData:
	coords[0].append(food["pos"][0])
	coords[1].append(food["pos"][1])
	sizes.append(50)
	if food["value"] == 5:
		colors.append("r")
	elif food["value"] == 10:
		colors.append("g")
	else:
		colors.append("b")
	fig.annotate(str((coords[0][-1], coords[1][-1])), (coords[0][-1], coords[1][-1]))



plt.scatter(coords[0], coords[1], s=sizes, marker='o', c=colors)
plt.show()

