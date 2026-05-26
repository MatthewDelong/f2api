import json
import os

file_path = r'c:\Users\Matthew Delong\Downloads\f1-telemetry-apis\f2api\drivers\2026\drivers.json'

with open(file_path, 'r', encoding='utf-8') as f:
    drivers = json.load(f)

nationalities = {
    "1": "brazilian",
    "2": "paraguayan",
    "3": "japanese",
    "4": "american",
    "5": "mexican",
    "6": "bulgarian",
    "7": "swedish",
    "8": "polish",
    "9": "italian",
    "10": "german",
    "11": "colombian",
    "12": "spanish",
    "14": "norwegian",
    "15": "irish",
    "16": "indian",
    "17": "thai",
    "20": "brazilian",
    "21": "british",
    "22": "argentine",
    "23": "mexican",
    "24": "dutch",
    "25": "british"
}

for num, data in drivers.items():
    if num in nationalities:
        data["Driver"]["nationality"] = nationalities[num]

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(drivers, f, indent=4, ensure_ascii=False)
