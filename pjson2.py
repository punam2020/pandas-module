import json

with open("my_json.json") as data_file:
    data = json.load(data_file)
    print(data)
    for i in range(0, len(data["people"])):
        print(data["people"][i]["id"])
with open("data.txt", "w") as outfile:
    json.dump(data, outfile)
