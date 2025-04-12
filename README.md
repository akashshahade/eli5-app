
# 🧸 Explain Like I'm 5 (ELI5)

This is a minimal, fast, and fun AI-powered web app that explains **any complex topic** like you're 5 years old.

Built using **Streamlit** and a **public Hugging Face model**, it runs entirely for free without any API keys.

---

## ✨ Features

- 🎯 Enter any question or topic (e.g., *What is blockchain?*)
- 🤖 Uses an open-source AI model to generate simple explanations
- 📄 Export the explanation as a PDF
- 🚀 Lightweight & deployable on Hugging Face Spaces or Streamlit Cloud

---

## 🛠️ Tech Stack

- Streamlit
- Transformers (`tiiuae/falcon-7b-instruct`)
- PyTorch
- FPDF

---

## 📦 Installation

```bash
git clone git clone https://huggingface.co/spaces/akashshahade/eli5-app
cd eli5-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 📄 Deployment

You can deploy this on [Hugging Face Spaces](https://huggingface.co/spaces) for free:

- Create a new Space (SDK = Streamlit)
- Upload `app.py` and `requirements.txt`
- That’s it! It builds automatically

---

## 📸 Screenshots

![screenshot](https://via.placeholder.com/800x400.png?text=ELI5+App+Screenshot)

---

## ❤️ Credits

Made with Love.  
By **Akash Shahade**
