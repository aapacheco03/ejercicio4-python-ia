# WFM Copilot 🛠️

**WFM Copilot** is an AI-powered application designed to support Workforce Management (WFM) and Operations leaders. It transforms operational data into actionable insights and professional communications.

## 🚀 Features

1.  **Feedback Sentiment Analyzer**: Analyzes agent or stakeholder feedback using HuggingFace Transformers (`distilbert-base-uncased-finetuned-sst-2-english`).
2.  **Executive Summary Generator**: Generates structured reports from operational metrics using the Google Gemini 2.0 Flash API.
3.  **Operations Communication Draft**: Drafts professional team announcements and situation-based communications using the Google Gemini 2.0 Flash API.

## 🛠️ Technologies Used

- **Interface**: [Gradio](https://gradio.app/)
- **NLP**: [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
- **LLM**: [Google Gemini API (google-genai SDK)](https://ai.google.dev/)
- **Language**: Python 3.x

## 📋 Prerequisites

To run the generative features (Summary and Communication), you need a Gemini API Key. You can get one for free at [Google AI Studio](https://aistudio.google.com/).

## ⚙️ Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd mi-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API Key:**
   - Windows (PowerShell): `$env:GEMINI_API_KEY = "YOUR_KEY_HERE"`
   - Linux/Mac: `export GEMINI_API_KEY="YOUR_KEY_HERE"`

4. **Run the app:**
   ```bash
   python app.py
   ```

## ☁️ Deployment on HuggingFace Spaces

1. Create a new **Gradio Space** on HuggingFace.
2. Upload `app.py`, `requirements.txt`, and `README.md`.
3. Go to **Settings > Variables and secrets**.
4. Add a new secret named `GEMINI_API_KEY` with your API key value.

---
Developed as a Final Project for the **Python for AI** Module.