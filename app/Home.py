import streamlit as st
import pandas as pd
from utils.ui_util import display_header
from utils.data_util import load_data

def filter_by_label(df):
    """Display dropdown and filter data based on selection."""
    unique_labels = ["All"] + sorted(df["label"].dropna().unique().tolist())
    selected_label = st.selectbox("Filter by Label", unique_labels)
    return df if selected_label == "All" else df[df["label"] == selected_label]


def search_posts(df, query):
    """Filter posts based on a search query."""
    if query:
        return df[df["content"].str.contains(query, case=False, na=False)]
    return df


def sort_posts(df):
    """Sort posts based on selected sorting criteria."""
    sort_options = {"Reactions": "reactions", "Comments": "comments"}
    selected_sort = st.selectbox("Sort by", list(sort_options.keys()), index=0)
    return df.sort_values(by=sort_options[selected_sort], ascending=False)


def home_page():
    """Display the Home Page."""
    display_header("Home Page", "🏠")
    st.write("Welcome to the LinkedIn Posts Categorization App!")
    st.header("Search Functionality")
    st.write(
        "This section includes a search feature for categorized LinkedIn posts.")
    search_query = st.text_input(
        "Enter your search query here:", key="search_query")
    return search_query


# Run the Home Page
search_query = home_page()

# Load the data once and cache it
df = load_data()

# Apply filters
filtered_df = filter_by_label(df)
searched_df = search_posts(filtered_df, search_query)
sorted_df = sort_posts(searched_df)

# User selects how many results to display
num_results = st.slider("Number of results to display:", 
                        min_value=1, max_value=50, value=5, step=1)

# Info/reminder to the user to help them see full post
st.info("*TIP: Double click a cell to view full text.*")

# Check if the number of instances is less than the selected number of results
if len(sorted_df) < num_results:
    if len(sorted_df) <= 1:
        st.warning(f"Only {len(sorted_df)} post found. Displaying the available post.")
    elif len(sorted_df) > 1:
        st.warning(f"Only {len(sorted_df)} posts found. Displaying all available posts.")

# Display DataFrame
st.dataframe(sorted_df[["content", "label", "reactions", "comments"]].head(
    num_results), use_container_width=True, hide_index=True)
