import json
import numpy as np
from PIL import Image, ImageDraw, ImageFont

categories = [
        "Person", "Ear", "Earmuffs", "Face", "Face-guard", "Face-mask-medical", "Foot", 
        "Tools", "Glasses", "Gloves", "Helmet", "Hands", "Head", "Medical-suit", 
        "Shoes", "Safety-suit", "Safety-vest"
    ]
    
id2label = dict(enumerate(categories))
label2id = {v: k for k, v in id2label.items()}

# 加載train.json文件
with open('train.json') as f:
    data = json.load(f)

data = data[70]
# 加載圖片
image_path = data["image"]  # 圖片路徑在train.json中的'image'鍵下
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

# 提取bbox和category信息
objects = data["objects"]
bbox_list = objects["bbox"]
category_list = objects["category"]

# 遍歷每個bbox和category，並在圖像上繪製
for i in range(len(bbox_list)):
    bbox = bbox_list[i]
    x_min, y_min, width, height = bbox  # bbox在COCO格式下：[x_min, y_min, width, height]

    # 計算右下角的座標
    x_max = x_min + width
    y_max = y_min + height

    # 繪製邊界框
    draw.rectangle([(x_min, y_min), (x_max, y_max)], outline="red", width=2)

    # 獲取類別ID並繪製類別名稱
    category_id = category_list[i]
    category_name = id2label[category_id] 
    print(category_name)
    font = ImageFont.load_default()

    draw.text((x_min, y_min), category_name, fill="white", font=font)

# 顯示圖片
image.show()
