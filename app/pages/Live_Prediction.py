import time
from utils.ui_util import display_header, display_model_info
from utils.model_util import load_model, predict_single_text
import streamlit as st

def making_label_prediction(user_input, model, tokenizer):
    """
    Accepts user input and predicts the category of the LinkedIn post.

    Args:
        user_input: The fetched text from user.
        model: The trained classification model.
        tokenizer: The tokenizer for text preprocessing.

    Displays:
        - A text area for user input.
        - A prediction result after processing the input.
    """
    # Initially, the text box is empty when the button is clicked
    if st.button("Predict", disabled=not user_input.strip()):
        with st.spinner("🔍 Predicting... Please wait."):
            time.sleep(1)  # Simulating prediction delay
            predicted_label = predict_single_text(user_input, model, tokenizer)
        
        # Show the predicted label with user input
        st.write(f"📝 User Input: **{user_input}**")
        st.success(f"🎯 Predicted Label: **{predicted_label}**")
        

def live_prediction_page(model_path, tokenizer_path):
    """
    Renders the Live Prediction Page for LinkedIn post classification.

    - Displays a header and instructions.
    - Loads the model and tokenizer.
    - Provides an interface for users to input text and receive predictions.

    Args:
    model_path: The hugging face model path for trained classification model.
    tokenizer_path: The tokenizer path for text preprocessing.

    """
    display_header("Live Prediction", "🔮")
    st.write("Enter a post in the chat box below to predict its category.")

    # Display model info
    display_model_info()

    # User text input area
    st.info("*TIP: The model performs better on longer texts - use at least 20 words.*")
    user_input = st.text_area("Enter your LinkedIn post text here:", height=100, key="user_input")

    # Instructional text
    st.info("Tip: Press `Ctrl + Enter` to lock your input after entering text.")
    
    # Load the model
    model, tokenizer = load_model(model_path, tokenizer_path)

    making_label_prediction(user_input, model, tokenizer)


# Model Path and Tokenizer
Hugging_Face_Model_Path = "mujtabakk/DistilBert-LinkedIn-Posts-Classfication"
Tokenizer_path = "../models/Distil_bert_tokenizer"

# Run the Live Prediction Page
live_prediction_page(Hugging_Face_Model_Path, Tokenizer_path)
