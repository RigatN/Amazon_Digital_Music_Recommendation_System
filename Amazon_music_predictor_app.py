# app.py

import streamlit as st
import pandas as pd
import os
import pickle

# Define the function to get recommendations
def get_recommendations(user_id, num_recommendations):
    # Load data
    music_review_fun = pd.read_csv("Data/music_review_fun.csv")
    music_meta = pd.read_csv("Data/music_meta.csv")
    
    # try:
    #     have_reviewed = list(music_review_fun.loc[user_id, 'asin'])
    # except KeyError:
    #     return "User ID not found or user hasn't reviewed any items."
    
    try:
        have_reviewed = list(music_review_fun.loc[music_review_fun['reviewerID'] == user_id, 'asin'])
        if len(have_reviewed) == 0:
            raise KeyError("User ID not found or user hasn't reviewed any items.")
    except KeyError as e:
        return str(e)


    not_reviewed = music_meta[~music_meta['asin'].isin(have_reviewed)].copy()
    not_reviewed.reset_index(inplace=True)

    if not_reviewed.empty:
        return "All items have been reviewed by the user."
    
    SVD_3 = pickle.load(open('SVD.sav', 'rb'))

    # Use loc to avoid SettingWithCopyWarning
    not_reviewed.loc[:, 'est_rating'] = not_reviewed['asin'].apply(lambda x: SVD_3.predict(user_id, x).est)
    not_reviewed.sort_values(by='est_rating', ascending=False, inplace=True)

    # Get top n recommendations
    recommendations = not_reviewed.head(num_recommendations)

    return recommendations

# Streamlit app
st.title("Amazon Music Recommender")
image_path = os.path.join("Images", "cover.PNG") 
st.image(image_path, caption='Amazon Music', use_column_width=True)

user_id = st.text_input("Enter User ID:")
num_recommendations = st.slider("Number of Recommendations", min_value=1, max_value=10, value=5)

if st.button("Get Recommendations"):
    if user_id:
        recommendations = get_recommendations(user_id, num_recommendations)
        if isinstance(recommendations, pd.DataFrame):
            st.write(recommendations)
        else:
            st.write(recommendations)
    else:
        st.warning("Please enter a User ID.")
