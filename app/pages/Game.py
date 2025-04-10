import time
import pandas as pd
from utils.ui_util import display_header
from utils.data_util import load_data
import streamlit as st

def initialize_session_state():
    """
    Initialize session state variables for the game.
    """
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "attempted" not in st.session_state:
        st.session_state.attempted = 3
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
    if "posts" not in st.session_state:
        st.session_state.posts = pd.DataFrame()

def load_and_sample_data():
    """
    Load the dataset and sample 3 random posts if no posts are currently loaded.
    """
    data = load_data()
    if st.session_state.posts.empty:
        st.session_state.posts = data.sample(n=3)
    return st.session_state.posts

def display_posts_and_collect_guesses(posts):
    """
    Display the posts and collect user guesses.
    """
    user_guesses = []
    for i, post in enumerate(posts.itertuples(), 1):
        st.subheader(f"Post {i}")
        st.write(post.content)
        guess = st.radio(
            f"What category does Post {i} belong to?",
            options=[
                "Professional Growth",
                "Events",
                "Interactive Promotions",
                "Educational Resources",
                "Trends",
                "Others"
            ],
            key=f"post_{i}",
            index=None
        )
        user_guesses.append(guess)
    return user_guesses

def calculate_score(user_guesses, posts):
    """
    Calculate the number of correct guesses and update the total score.
    """
    correct_guesses = sum(
        user_guesses[i] == post.label
        for i, post in enumerate(posts.itertuples())
    )
    st.session_state.score += correct_guesses
    return correct_guesses

def display_results(correct_guesses):
    """
    Display the results of the user's guesses with custom messages and emojis.
    """
    if correct_guesses == 3:
        st.success("🎉 Perfect! You got 3 out of 3 correct! 🎉")
        st.balloons()
    elif correct_guesses == 2:
        st.warning("😊 Good job! You got 2 out of 3 correct. Keep trying!")
    elif correct_guesses == 1:
        st.warning("🤔 Not bad! You got 1 out of 3 correct. You can do better!")
    else:
        st.error("😢 Better luck next time! You got 0 out of 3 correct.")

    # Display the total score
    st.write(f"Your Score: {st.session_state.score}")

def load_quiz_again():
    """
    Loads a new quiz with sampled questions.
    """

    # Add a "Play Again" button
    if st.button("Play Again"):

        # Reset the posts and rerun the app
        st.session_state.posts = pd.DataFrame()
        st.success("🔄 New quiz loaded!")
        if st.session_state.submitted:
          st.session_state.attempted += 3
        time.sleep(0.7)
        st.rerun()


def game_page():
    """
    Display the Game Page. This function orchestrates the game logic and UI.
    """
    display_header("LinkedIn Post Categorization Game", "🎮")
    st.write("Guess the category for each post and see how many you get right!")

    # Initialize session state
    initialize_session_state()

    # Load and sample data
    posts = load_and_sample_data()

    # Display posts and collect user guesses
    user_guesses = display_posts_and_collect_guesses(posts)

    # Submit button
    if st.button("Submit"):
        # Calculate score
        correct_guesses = calculate_score(user_guesses, posts)

        # Display results
        display_results(correct_guesses)

        st.session_state.submitted = True


    # Display the score in the sidebar
    st.sidebar.write(f"Total Quiz Score: {st.session_state.score} / {st.session_state.attempted}")

# Run the Game Page
game_page()

load_quiz_again()