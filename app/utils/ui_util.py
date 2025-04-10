import streamlit as st

def display_header(title: str, icon: str):
    """
    Display a header with a title and icon.

    Args:
        title (str): Title of the page.
        icon (str): Icon for the page.
    """
    st.set_page_config(page_title=title, page_icon=icon)
    st.title(f"{icon} {title}")

def display_model_info():
    """
    Display model information in an expandable section.
    """
    with st.expander("ℹ️ **Model Information**"):
        st.markdown("""
        - **Model:** DistilBERT (Fine-tuned on LinkedIn Influencers Dataset)
        - **Accuracy:** 75.31%
        - **F1 Score:** 75.55%
        """)