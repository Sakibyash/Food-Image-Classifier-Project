🍽️ Food Image Classifier

Welcome to the Food Image Classifier! This project leverages state-of-the-art deep learning techniques to classify food images into different categories. It is built using FastAI and PyTorch, and seamlessly deployed using Gradio on Hugging Face Spaces for an interactive user experience.

🚀 Features

✅ Accurate Food Classification - Identifies multiple food categories with high precision.✅ Powered by ResNet50 - Utilizes a fine-tuned ResNet50 model for robust classification.✅ Seamless Deployment - Hosted on Hugging Face Spaces for quick and easy access.✅ User-Friendly Web Interface - Integrated with GitHub Pages for an enhanced user experience.✅ Detailed Food Information - Displays dish details such as ingredients and descriptions.

🌐 Live Demo

Try out the Food Image Classifier here:🔗 Hugging Face Spaces: Food Image Classifier🔗 GitHub Pages: Food Image Classifier Web

🖼️ Interface Preview



📂 Project Structure

Food-Image-Classifier-Project/
│-- Data/         # Dataset used for training
│-- Dataloaders/  # Scripts for loading and preprocessing data
│-- Deployments/  # Deployment-related files
│-- Models/       # Trained models
│-- Notebook/     # Jupyter notebooks for experimentation
│-- App/          # Web application code
│-- README.md     # Documentation

🛠️ How It Works

1️⃣ Users upload a food image through the web interface.2️⃣ The image is processed and sent to the Hugging Face API.3️⃣ The model predicts the dish category using ResNet50.4️⃣ Relevant dish details (ingredients, description) are displayed.5️⃣ The result is shown with the uploaded image on the webpage.

💻 Installation

To run this project locally, follow these steps:

git clone https://github.com/Sakibyash/Food_image_classifier.git
cd Food_image_classifier
pip install -r requirements.txt
python app.py

Then, open index.html in your browser.

🧠 Model Details

🍛 Identifies 34 different dishes from various cuisines.📷 Dataset - 24,000 images used for training.🤖 Model - ResNet50 fine-tuned with FastAI.📊 Applications - Ideal for menu recommendations & inventory management.🏗️ Training Framework - FastAI + PyTorch.☁️ Deployment - Hugging Face Spaces for easy access.

🔗 API Usage

You can access the prediction API directly using Python:

import requests

url = "https://huggingface.co/spaces/Sakibrumu/Food_image_classifier_Final"
files = {"file": open("example.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())

🤝 Contribution

We welcome contributions! Feel free to open an issue or submit a pull request to improve functionality, add new features, or enhance the dataset.

📜 License

This project is licensed under the MIT License.

Developed by: MD. Sakib Hasan

🖼️ Demo Images






