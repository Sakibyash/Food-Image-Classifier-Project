# 🍽️ Food Image Classifier

Welcome to the **Food Image Classifier**! This project utilizes cutting-edge **deep learning** techniques to classify food images with high accuracy. Built using **FastAI** and **PyTorch**, it is seamlessly deployed using **Gradio** on **Hugging Face Spaces** for an interactive user experience.

---

## 🚀 Features

✨ **High-Accuracy Food Classification** - Identifies multiple food categories with precision.  
🖼️ **AI-Powered Image Recognition** - Recognizes 34 different food items from various cuisines.  
⚡ **Powered by ResNet50** - Uses **ResNet50**, a powerful deep learning model for classification.  
🌍 **Deployed on Hugging Face Spaces** - Easily accessible with a simple web interface.  
📜 **Detailed Food Information** - Displays dish details, ingredients, and nutritional facts.  
🛠 **FastAI + PyTorch Framework** - Robust and efficient training setup.  

---

## 🌐 Live Demo

🎯 Try out the **Food Image Classifier** here:  
🔗 **[Hugging Face Spaces](https://huggingface.co/spaces/Sakibrumu/Food_image_classifier_Final)**  
🔗 **[GitHub Pages Web App](https://sakibyash.github.io/Food-image-Classifier_/)**

### 🖼️ Interface Preview
![Food Image Classifier](https://your-image-link.com/interface-preview.jpg)

---

## 📂 Project Structure
```
📂 Food-Image-Classifier-Project/
├── 📁 Data/          # Dataset used for training
├── 📁 Dataloaders/   # Scripts for data preprocessing
├── 📁 Deployments/   # Deployment-related files
├── 📁 Models/        # Trained deep learning models
├── 📁 Notebook/      # Jupyter notebooks for model experimentation
├── 📁 App/           # Web application files
├── 📜 README.md      # Documentation
```

---

## 🛠️ How It Works

1️⃣ **Upload an image** through the web interface.  
2️⃣ **Image is processed** and sent to the model for classification.  
3️⃣ **AI predicts the dish category** using a **ResNet50 model**.  
4️⃣ **Dish details and ingredients** are retrieved and displayed.  
5️⃣ **Results & uploaded image** appear on the webpage.  

---

## 💻 Installation Guide

Want to run this project locally? Follow these simple steps:

```bash
git clone https://github.com/Sakibyash/Food_image_classifier.git
cd Food_image_classifier
pip install -r requirements.txt
python app.py
```

Then, open `index.html` in your browser. 🚀

---

## 🧠 Model Details

🍛 **Recognizes 34+ Food Items** - Covers a diverse range of cuisines.  
📷 **Dataset** - Over 24,000 high-quality images used for training.  
🤖 **Deep Learning Model** - Fine-tuned **ResNet50** on FastAI.  
📊 **Use Cases** - Ideal for **menu recommendations** & **restaurant automation**.  
🏗️ **Training Framework** - **FastAI + PyTorch** for high-speed performance.  
☁️ **Deployment** - Hosted on **Hugging Face Spaces**.  

---

## 🔗 API Usage

You can integrate the model using its API:

```python
import requests

url = "https://huggingface.co/spaces/Sakibrumu/Food_image_classifier_Final"
files = {"file": open("example.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

---

## 🤝 Contribution

👨‍💻 Want to improve this project? Contributions are welcome! Open an **issue** or submit a **pull request** to enhance features, improve accuracy, or expand the dataset.

---

## 📜 License

This project is **open-source** and licensed under the **MIT License**.

📌 **Developed by:** MD. Sakib Hasan  

---

### 🖼️ Demo Images
![Demo 1](Screenshot%202025-02-18%20015452.png)
![Demo 2](Screenshot%202025-02-18%20015510.png)
![Demo 3](Screenshot%202025-02-18%20015723.png)
![Demo 4](Screenshot%202025-02-18%20015746.png)

🚀 **Try it out and start recognizing food instantly!**
