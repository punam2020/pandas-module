import json

raw_data = """
{ "city":["bmp","bbsr","delhi","mumbai"],
"rank":["1st","2nd","3rd","4th"],
"score":[56,67,78,89]
}
"""
data = json.loads(raw_data)
print(data["city"][0])
print(json.dumps(data))
