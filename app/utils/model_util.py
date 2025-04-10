import torch
from transformers import AutoModelForSequenceClassification, DistilBertTokenizer
import streamlit as st

@st.cache_data
def load_model(model_name: str, tokenizer_path: str):
    """
    Load the pre-trained model and tokenizer.

    Args:
        model_name (str): Name of the pre-trained model.
        tokenizer_path (str): Path to the tokenizer.

    Returns:
        tuple: (model, tokenizer)
    """
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = DistilBertTokenizer.from_pretrained(tokenizer_path)
    return model, tokenizer

def predict_single_text(text: str, model, tokenizer) -> str:
    """
    Predict the category of a LinkedIn post.

    Args:
        text (str): Input text (LinkedIn post).
        model: Pre-trained model.
        tokenizer: Tokenizer for the model.

    Returns:
        str: Predicted category.
    """
    model.eval()
    encoding = tokenizer(
        text, max_length=128, padding="max_length",
        truncation=True, return_tensors="pt",
    )
    input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        preds = torch.argmax(outputs.logits, dim=1).cpu().detach().numpy()

    index_label_mapping = {
        1.0: "Professional Growth",
        2.0: "Events",
        3.0: "Interactive Promotions",
        4.0: "Educational Resources",
        5.0: "Trends",
        0.0: "Others"
    }
    return index_label_mapping[preds[0]]