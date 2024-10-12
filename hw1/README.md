## CVPDL HW1
### Installation Instructions

#### 1. Create Conda Environment
```bash
conda create -y -n hw1 python=3.10
conda activate hw1
```
#### 2. Pip install some packages
```bash
pip install -r requirements.txt 
```

#### 3. Download dataset and MMdetection
```bash
bash download.sh
```
### Train
```bash
bash train.sh
```
：model will be saved under mmdetection/work_dirs/deformable-detr_r50_16xb2-50e_coco

### Infer

#### On validation dataset
```bash
bash infer_valid.sh
```
：result wiil be saved as **final_output_valid.json** in current folder

#### On testing dataset
```bash
bash infer_test.sh
```
：result wiil be saved as **final_output_test.json** in current folder

### Evaluation

#### On validation dataset
```python 
python eval.py final_output_valid.json ./valid_target.json
```


