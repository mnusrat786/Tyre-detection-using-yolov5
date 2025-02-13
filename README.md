# 🚗 AutoTyreDetect 🛞  
A **YOLOv5-based Tyre Detection** model trained on a custom dataset.

---

## 📌 1️⃣ Setup Instructions

### 🔹 **Step 1: Clone the Repository**
First, download the repository:
```bash
git clone https://github.com/mnusrat786/AutoTyreDetect.git
cd AutoTyreDetect
```

### 🔹 **Step 2: Install Dependencies**
Ensure you have **Python 3.8+** installed, then install dependencies:
```bash
pip install -r requirements.txt
```

### 🔹 **Step 3: Install YOLOv5**
We use **Ultralytics' YOLOv5**. Clone and install it:
```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
cd ..
```

---

## 📌 2️⃣ Dataset Structure

### 🔹 **Step 1: Dataset Organization**
Your dataset is stored in `data/dataset/` and follows this structure:
```bash
data/
├── dataset/
│   ├── images/          # All tyre images
│   │   ├── train/       # Training images
│   │   ├── val/         # Validation images
│   ├── labels/          # YOLO annotation files
│   │   ├── train/       # Training labels
│   │   ├── val/         # Validation labels
│   ├── dataset.yaml     # YOLOv5 dataset config
```

### 🔹 **Step 2: Verify the Dataset**
Ensure your dataset has:
- **Images stored inside `images/train/` and `images/val/`**
- **Labels (annotations) stored inside `labels/train/` and `labels/val/`**
- **A valid `dataset.yaml` file**

---

## 📌 3️⃣ Training the YOLOv5 Model

### 🔹 **Step 1: Start Training**
To train YOLOv5 on your dataset, run:
```bash
python yolov5/train.py --img 640 --batch 16 --epochs 50 --data data/dataset/dataset.yaml --weights yolov5s.pt
```

### 🔹 **Step 2: Training Parameters Explained**
- `--img 640` → Image size (YOLOv5 default is 640x640)  
- `--batch 16` → Batch size for training  
- `--epochs 50` → Number of training epochs  
- `--data data/dataset/dataset.yaml` → Dataset configuration file  
- `--weights yolov5s.pt` → Pretrained YOLOv5 model  

---

## 📌 4️⃣ Running Inference (Tyre Detection)

### 🔹 **Step 1: Run Detection on an Image**
Once the model is trained, run inference to **detect tyres** on new images:
```bash
python yolov5/detect.py --weights yolov5/runs/train/exp/weights/best.pt --source path/to/your/test/image.jpg
```
Replace `path/to/your/test/image.jpg` with the actual image path.

### 🔹 **Step 2: Run Detection on a Video**
To detect tyres in a video, use:
```bash
python yolov5/detect.py --weights yolov5/runs/train/exp/weights/best.pt --source path/to/your/video.mp4
```

---

## 📌 5️⃣ Model Results

### 🔹 **Step 1: Check Training Results**
After training, your results and weights will be stored in:
```bash
yolov5/runs/train/exp/
├── weights/       # Best trained model
├── labels/        # Detection results
├── results.png    # YOLOv5 training performance graph
```

### 🔹 **Step 2: Locate the Final Trained Model**
The final trained model will be:
```bash
yolov5/runs/train/exp/weights/best.pt
```

---

## 📌 6️⃣ How to Use the Trained Model

### 🔹 **Step 1: Run Inference on a New Image**
If you want to use the trained model on new images, run:
```bash
python yolov5/detect.py --weights yolov5/runs/train/exp/weights/best.pt --source path/to/your/image.jpg
```
This will **detect tyres** and display the image with bounding boxes.

---

## 📌 7️⃣ Contributors & Issues

### 🔹 **Step 1: Contribute to the Project**
If you want to improve the project, feel free to fork the repository and submit a pull request.

### 🔹 **Step 2: Report Issues**
If you find any issues, please **open a GitHub issue** describing the problem.

---

## 📌 8️⃣ References

### 🔹 **Step 1: External Resources**
- [YOLOv5 Official Repository](https://github.com/ultralytics/yolov5)  
- [LabelImg (For Data Annotation)](https://github.com/heartexlabs/labelImg)  

---
