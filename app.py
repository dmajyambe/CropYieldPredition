import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import plotly.express as px
import os 


st.title("Crop Yield Prediction")

data = pd.read_csv("crop_yields.csv")

cols = ['year', 'bean_yield', 'cassava_yield', 'cereal_yield', 'coffee_yield', 'fruit_yield',
        'groundnut_yield', 'maize_yield', 'millet_yield', 'pea_yield', 'plantains_yield',
        'potato_yield', 'pulses_yield', 'pumpkins__squash_and_gourds_yield',
        'pyrethrum__dried_flowers_yield', 'roots_and_tubers_yield', 'sorghum_yield',
        'soybean_yield', 'sugarcane_yield', 'sugar_crops_yield', 'sweet_potatoes_yield',
        'taro_yield', 'tea_yield', 'tobacco_yield', 'vegetables_yield', 'wheat_yield',
        'yams_yield']

# Select the row for Rwanda and the specified columns
data = data.loc[data['country'] == "Rwanda", cols]

# Handle missing values by imputing with the mean
data.fillna(data.mean(), inplace=True)

# Train the model for all crops
models = {}
for crop in cols[1:]:
    X = data[['year']]
    y = data[crop]

    # Split the data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    models[crop] = model

nav = st.sidebar.radio("NAVIGATION", ['Home', "Prediction", "Real-time Data Access","Your feedback"])

if nav == 'Home':
    st.write('Home')
    st.image("pastel-moon.jpg", width=400)
    if st.checkbox("Show yields in table"):
        st.table(data)

    crops = st.selectbox("Select crop type", cols[1:])
    data_plot = data[['year', crops]]
    graph = st.checkbox("Show yield plot")
    if graph:
        fig = px.line(data_plot, x='year', y=crops, title=f'{crops}  in Rwanda over the Years')
        fig.update_layout(legend_title_text='Yield', legend_orientation='h')
        st.plotly_chart(fig) 

if nav == 'Prediction':
    st.header("Predict Your Yield")
    crops_to_predict = st.selectbox("Select crop type to predict yield", cols[1:])
    year_to_predict = st.number_input("Enter the year for yield prediction", min_value=int(data['year'].min()),
                                      max_value=int(data['year'].max()) + 5, step=1)
    model = models[crops_to_predict]
    prediction = model.predict([[year_to_predict]])
    st.write(f"The predicted  {crops_to_predict} in the year {year_to_predict} is {prediction[0]:.2f} tonnes per hectare")

#customer feedback
if nav=="Your feedback":
    
    feedback_type = st.radio("Feedback Type", ("General", "Bug Report", "Feature Request"))
    name = st.text_input("Your Name (optional)", "")
    email = st.text_input("Your Email(optional)", "")
    feedback_message = st.text_area("Feedback Message", height=150)
    rating = st.slider("Rate us (1-10)", min_value=1, max_value=10, step=1)
    submit_button = st.button("Submit")



    if submit_button:
        feedback_data = {
            "Name": name,
            "Email": email,
            "Feedback": feedback_message,
            "Feedback type": feedback_type,
            "Rating": rating
        }

        feedback_df = pd.DataFrame([feedback_data])

        # Check if "feedback_data.csv" file exists and is non-empty before reading it
        if os.path.isfile("feedback_data.csv") and os.path.getsize("feedback_data.csv") > 0:
            try:
                existing_feedback_df = pd.read_csv("feedback_data.csv")
                feedback_df = pd.concat([existing_feedback_df, feedback_df], ignore_index=True)
            except pd.errors.EmptyDataError:
                pass

        feedback_df.to_csv("feedback_data.csv", index=False)

        st.success("Thank you for your valued feedback, " + name)