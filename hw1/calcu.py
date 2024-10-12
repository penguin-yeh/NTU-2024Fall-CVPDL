import json
import string
import os

goal = {"images":[], "annotations":[], "categories":[]}

sum = [0] * 17

goal["categories"] = [
    {"id": 0, "name": "Person"},
    {"id": 1, "name": "Ear"},
    {"id": 2, "name": "Earmuffs"},
    {"id": 3, "name": "Face"},
    {"id": 4, "name": "Face-guard"},
    {"id": 5, "name": "Face-mask-medical"},
    {"id": 6, "name": "Foot"},
    {"id": 7, "name": "Tools"},
    {"id": 8, "name": "Glasses"},
    {"id": 9, "name": "Gloves"},
    {"id": 10, "name": "Helmet"},
    {"id": 11, "name": "Hands"},
    {"id": 12, "name": "Head"},
    {"id": 13, "name": "Medical-suit"},
    {"id": 14, "name": "Shoes"},
    {"id": 15, "name": "Safety-suit"},
    {"id": 16, "name": "Safety-vest"}
]

with open('train.json', 'r', encoding='utf-8') as file:
    dataset = json.load(file)
    
for data in dataset:
        
    objects = data["objects"]
    for category in (objects['category']):
        print(category)
        sum[category] += 1
            
            
print(sum)