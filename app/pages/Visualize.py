import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from utils.ui_util import display_header
from utils.data_util import load_data
from string import punctuation

# Initialize the important variables needed for this page
data = load_data()
categories = data['label'].unique().tolist()
visual_options = ["Word Cloud", "Top 10 words", "Post Length"]
# Custom stop words: Cut out a few extra stop words + quirk words from data
w = WordCloud()
stop_words = list(w.stopwords)
custom_stop_words = ['see', 'more', 'https', 'lnkd', 's', 'time', 'will', 'us', '…see', 'one', 'get']
stop_words = set(stop_words + custom_stop_words)


display_header("Visualize your Linkedin Data", "📊")

# Radio buttons to select visual type
selected_visual = st.radio("Select Visualization Type", visual_options)

# Select Category. If Visual type is 'Post Length', we also give the option to display an overlapping histogram
if selected_visual == "Post Length":
    category_options = ["All Categories"] + data['label'].unique().tolist()
    selected_category = st.selectbox("Select a Category", category_options)
else:
    categories = data['label'].unique().tolist()
    selected_category = st.selectbox("Select a Category", categories)

# Visualization logic based on the selected visual type
if selected_visual == "Word Cloud":
    st.subheader(f"Word Cloud for '{selected_category}'")
    # Filter data by the selected category
    filtered_data = data[data['label'] == selected_category]
    text = " ".join(filtered_data['content'].tolist())
    wordcloud = WordCloud(width=800, height=400, background_color="white", stopwords=stop_words).generate(text)
    # Plot the word cloud
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

elif selected_visual == "Top 10 words":
    st.subheader(f"Top Words Frequency for '{selected_category}'")
    filtered_data = data[data['label'] == selected_category]
    text = " ".join(filtered_data['content'].tolist())
    words = text.split()
    punc_set = set([punc for punc in punctuation])
    words = [word.lower() for word in words if word.lower() not in stop_words and word not in punc_set and word.lower() not in stop_words]
    word_freq = Counter(words)
    common_words = word_freq.most_common(10)
    freq_df = pd.DataFrame(common_words, columns=["Word", "Frequency"])
    st.bar_chart(freq_df.set_index("Word"), horizontal=True)

elif selected_visual == "Post Length":
    if selected_category == "All Categories":
        st.subheader("Comparative Length Distributions Across All Categories")
        num_cols = 2
        for i, cat in enumerate(categories):
    # Create a new row of columns for every `num_cols` categories
            if i % num_cols == 0:
                cols = st.columns(num_cols)
            with cols[i % num_cols]:
                subset = data[data['label'] == cat]
                # Calculate post length (in words) for each post
                lengths = subset['content'].apply(lambda x: len(str(x).split()))
                # Create a separate figure for this category
                fig, ax = plt.subplots(figsize=(5, 4))
                ax.hist(lengths, bins=20, alpha=0.7)
                ax.set_title(cat)
                ax.set_xlabel("Post Length (words)")
                ax.set_ylabel("Frequency")
                st.pyplot(fig)
    else:
        st.subheader(f"Post Length Distribution for '{selected_category}'")
        filtered_data = data[data['label'] == selected_category]
        lengths = filtered_data['content'].apply(lambda x: len(str(x).split()))
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.hist(lengths, bins=50, alpha=0.7)
        ax.set_xlabel("Post Length (words)")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)