import streamlit as st
import pandas as pd

def feedback_form():
    st.header("Feedback Form")
    
    # Input fields for the feedback form
    name = st.text_input("Name", "")
    email = st.text_input("Email", "")
    feedback = st.text_area("Feedback", "")
    rating = st.slider("Rating", min_value=1, max_value=5, step=1)
    submit_button = st.button("Submit")

    # Check if the submit button is clicked and store the data
    if submit_button:
        feedback_data = {
            "Name": name,
            "Email": email,
            "Feedback": feedback,
            "Rating": rating
        }

        # Append the feedback data to a DataFrame
        feedback_df = pd.DataFrame([feedback_data])

        # Load existing feedback data if available, or create a new DataFrame
        try:
            existing_feedback_df = pd.read_csv("feedback_data.csv")
            feedback_df = pd.concat([existing_feedback_df, feedback_df], ignore_index=True)
        except FileNotFoundError:
            pass

        # Save the feedback data to a CSV file
        feedback_df.to_csv("feedback_data.csv", index=False)

        st.success("Feedback submitted successfully!")
if __name__ == "__main__":
    feedback_form()
