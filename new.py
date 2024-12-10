import streamlit as st

# Title of the App
st.title("Big-Small Prediction Tool")

# Input Section
st.header("Enter the Last 5 Outcomes")
outcomes = []
for i in range(5):
    outcomes.append(st.selectbox(f"Outcome {i + 1}:", ["Big", "Small"], key=i))

# Prediction Logic
if st.button("Predict Next Outcome"):
    big_count = outcomes.count("Big")
    small_count = outcomes.count("Small")
    
    if big_count > small_count:
        prediction = "Small"
    else:
        prediction = "Big"
    
    st.success(f"The Predicted Next Outcome is: {prediction}")

# Footer
st.info("This tool predicts the next outcome based on the trend of the last 5 results.")
