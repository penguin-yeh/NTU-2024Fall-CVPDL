import pickle
import os
import torch
import json
import argparse

parser = argparse.ArgumentParser(description='Filter by scores')
parser.add_argument('input_file', type=str, help='file that is filtered')
parser.add_argument('output_file', type=str, help='filtered result')


args = parser.parse_args()


with open(args.input_file, 'r', encoding='utf-8') as file:
    dataset = json.load(file)
    
goal = {}
score_threshold = 0.3

for key, value in dataset.items():
    
    data = {"boxes":[], "labels":[], "scores":[]}
    image_name = key
    boxes = value["boxes"]
    labels = value["labels"]
    scores = value["scores"]
    
    for box, label, score in zip(boxes, labels, scores):
        if score > score_threshold:
            data["boxes"].append(box)
            data["labels"].append(label)
            data["scores"].append(score)
            
    goal[image_name] = data
    
with open(args.output_file, 'w') as json_file:
    json.dump(goal, json_file, indent=4)

print("filtered!!!!")