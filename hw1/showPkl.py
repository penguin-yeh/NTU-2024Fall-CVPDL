import pickle
import os
import torch
import json
import argparse

parser = argparse.ArgumentParser(description='Process two text files.')
parser.add_argument('input_file', type=str, help='file that is predicted')
parser.add_argument('output_file', type=str, help='predicted result')

args = parser.parse_args()

f = open(args.input_file,'rb')
outputs = pickle.load(f)

goal={}

for output in outputs:
    # print(output)
    file_name = os.path.basename(output["img_path"])
    data = {"boxes": output["pred_instances"]["bboxes"].tolist(), 
            "labels": output["pred_instances"]["labels"].tolist(),
            "scores": output["pred_instances"]["scores"].tolist()}
    
    goal[file_name] = data
    
with open(args.output_file, 'w') as json_file:
    json.dump(goal, json_file, indent=4)

print("Saved!!!!")
    
    
    