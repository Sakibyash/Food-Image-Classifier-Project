🍽️ Food Image Classifier

Welcome to the Food Image Classifier! This project utilizes deep learning to classify food images into different categories. It is powered by FastAI, PyTorch, and deployed using Gradio on Hugging Face Spaces.



🚀 Features

✅ Classifies food images into multiple categories with high accuracy.

🔥 Uses ResNet50 as the backbone model for classification.

🌍 Deployed on Hugging Face Spaces for easy accessibility.

🖥️ Integrated with GitHub Pages to provide a user-friendly web interface.

📜 Displays additional dish details such as ingredients and descriptions.


🌐 Live Demo

Try out the classifier here: Food Image Classifier on Hugging Face



📂 Project Structure

Food-Image-Classifier-Project/
│-- Data/           # Dataset used for training
│-- Dataloaders/    # Scripts for loading and preprocessing data
│-- Deployments/    # Deployment-related files
│-- Models/         # Trained models
│-- Notebook/       # Jupyter notebooks for experimentation
How its Look 
![Food Image Classifier](https://raw.githubusercontent.com/Sakibyash/Food_image_classifier/main/image.jpg)

🛠️ How It Works

1. 📤 Users upload a food image through the web interface.


2. 🔍 The image is sent to the Hugging Face API, where the model predicts the dish category.


3. 🎯 The predicted label is displayed along with relevant details from dish_details.json.


4. 🖼️ The uploaded image and classification result are shown on the web page.



💻 Installation

If you want to run this project locally, follow these steps:

git clone https://github.com/Sakibyash/Food_image_classifier.git
cd Food_image_classifier
pip install -r requirements.txt
python app.py

Then, open index.html in your browser.

🧠 Model Details

🍛 Identifies 34 varieties of appetizers from Indian and Western cuisines.

📷 Dataset: 24,000 images for robust training.

🤖 Model: ResNet50 fine-tuned with FastAI

📊 Applications: Ideal for menu recommendations and inventory management.

🏗️ Training Framework: FastAI + PyTorch

☁️ Deployment: Hugging Face Spaces

🤖 Model: ResNet50 fine-tuned with FastAI

📊 Dataset: A curated dataset of various food items

🏗️ Training Framework: FastAI + PyTorch

☁️ Deployment: Hugging Face Spaces


🔗 API Usage

You can access the prediction API directly using:

import requests

url = "https://huggingface.co/spaces/Sakibrumu/Food_Image_Classification"
files = {"file": open("example.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())

🤝 Contribution

Feel free to contribute to this project! Open an issue or submit a pull request to improve functionality.

📜 License

This project is licensed under the MIT License.


---

Developed by MD. Sakib Hasan

