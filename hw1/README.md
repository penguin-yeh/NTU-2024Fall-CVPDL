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
you will see two files： **mmdetection.zip**, **model.pth** once finish. If don't, please download them using below links：<br>
[mmdetection.zip](https://drive.google.com/uc?id=1Q-0tsPR3Yk3RXULOsAVfMpQ00-3Uxbwl)<br>
[model.pth](https://drive.google.com/uc?id=1u_XYDUZY4GwdlemSf3YZI65H3Wo0mCTr)

#### 4. Install additional packages
```bash
bash install.sh
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
：result wiil be saved as **valid_r12922016.json** in current folder

#### On testing dataset
```bash
bash infer_test.sh
```
：result wiil be saved as **test_r12922016.json** in current folder

### Evaluation

#### On validation dataset
```python 
python eval.py valid_r12922016.json ./valid_target.json
```


