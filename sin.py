import numpy as np
import json

# generate evenly spaced numbers from 0 to 6pi
x = np.linspace(0, 6 * np.pi, 1000)

# make a sinus function out of them
y = np.sin(x)

# printing the values for debug purposes
# print(f"x = {x}\ny = {y}")

# store x and y in json file for easier work
with open("sin.json", "r") as json_file:
    data = json.load(json_file)

# convert json file to ndjson for kibana
with open("sin.ndjson", "w") as ndjson_file:
    for item in data:
        ndjson_file.write(json.dumps(item) + '\n')
