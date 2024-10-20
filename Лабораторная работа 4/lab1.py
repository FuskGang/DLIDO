# TODO решите задачу
import json

def task() -> float:
    with open("input.json", "r") as f:
        data = json.loads(f.read())

    sm = 0

    for dict_info in data:
        sm += (dict_info["score"] * dict_info["weight"])

    return round(sm, 3)

print(task())
