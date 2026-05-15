import os
import gradio as gr
from google import genai
from transformers import pipeline

# --- Configuration & Initialization ---
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)
    GEMINI_MODEL = 'gemini-2.0-flash'
else:
    client = None

try:
    sentiment_analyzer = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
except Exception:
    sentiment_analyzer = None

def analyze_sentiment(text):
    if not text.strip(): return 'Please provide feedback text.', '', ''
    if not sentiment_analyzer: return 'Sentiment model not available.', '', ''
    result = sentiment_analyzer(text)[0]
    label = result['label']
    score = f"{result['score']:.2%}"
    interpretation = 'Positive sentiment indicates stable morale.' if label == 'POSITIVE' else 'Negative sentiment detected.'
    return label, score, interpretation

def generate_executive_summary(metrics):
    if not metrics.strip(): return 'Please provide operational metrics.'
    if not client: return 'Gemini API key not configured.'
    prompt = f'As a WFM Expert, analyze these metrics and provide a structured report: {metrics}'
    try:
        response = client.models.generate_content(model=GEMINI_MODEL, contents=prompt)
        return response.text
    except Exception as e:
        return f'Error: {str(e)}'

def draft_communication(situation):
    if not situation.strip(): return 'Please provide context.'
    if not client: return 'Gemini API key not configured.'
    prompt = f'Draft a professional communication for: {situation}'
    try:
        response = client.models.generate_content(model=GEMINI_MODEL, contents=prompt)
        return response.text
    except Exception as e:
        return f'Error: {str(e)}'

with gr.Blocks(title='WFM Copilot') as demo:
    gr.Markdown('# 🛠️ WFM Copilot')
    with gr.Tabs():
        with gr.TabItem('📊 Sentiment Analyzer'):
            sentiment_input = gr.Textbox(label='Feedback', lines=3)
            sentiment_btn = gr.Button('Analyze')
            sentiment_label = gr.Textbox(label='Sentiment')
            sentiment_score = gr.Textbox(label='Score')
            sentiment_interpret = gr.Textbox(label='Interpretation')
            sentiment_btn.click(analyze_sentiment, inputs=sentiment_input, outputs=[sentiment_label, sentiment_score, sentiment_interpret])
        with gr.TabItem('📝 Executive Summary'):
            summary_input = gr.Textbox(label='Metrics', lines=4)
            summary_btn = gr.Button('Generate')
            summary_output = gr.Markdown()
            summary_btn.click(generate_executive_summary, inputs=summary_input, outputs=summary_output)
        with gr.TabItem('📧 Communication Draft'):
            comm_input = gr.Textbox(label='Situation', lines=4)
            comm_btn = gr.Button('Draft')
            comm_output = gr.Markdown()
            comm_btn.click(draft_communication, inputs=comm_input, outputs=comm_output)

if __name__ == '__main__':
    demo.launch()
