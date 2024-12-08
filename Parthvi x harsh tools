import streamlit as st
import random
import pandas as pd

# Initialize or Load Trends
if "trends" not in st.session_state:
    st.session_state["trends"] = []

if "loss_count" not in st.session_state:
    st.session_state["loss_count"] = 0

# Title of the App
st.title("Big-Small Prediction Tool (Smart & Adaptive)")

# Input Section
st.header("Enter the Number of Outcomes")
num_outcomes = st.number_input("How many past outcomes do you want to analyze?", min_value=3, max_value=20, value=5)

st.subheader("Enter the Last Outcomes")
outcomes = []
for i in range(int(num_outcomes)):
    outcomes.append(st.selectbox(f"Outcome {i + 1}:", ["Big", "Small"], key=f"outcome_{i}"))

# Prediction Logic
if st.button("Predict Next Outcome"):
    # Count occurrences
    big_count = outcomes.count("Big")
    small_count = outcomes.count("Small")
    
    # Determine Prediction
    if st.session_state["loss_count"] < 2:  # Normal prediction logic
        if big_count > small_count:
            prediction = "Small"
        elif big_count < small_count:
            prediction = "Big"
        else:
            prediction = random.choice(["Big", "Small"])
    else:  # After 2 losses, prioritize a win
        prediction = "Big" if outcomes[-1] == "Small" else "Small"
        st.session_state["loss_count"] = 0  # Reset loss count after win
    
    # Display Prediction
    st.success(f"The Predicted Next Outcome is: {prediction}")
    
    # Update Trends and Track Results
    st.session_state["trends"].append({"Outcomes": outcomes, "Prediction": prediction})
    st.write("Saved Trends:")
    st.dataframe(pd.DataFrame(st.session_state["trends"]))
    
    # Check for Accuracy
    if len(st.session_state["trends"]) > 1:
        previous_outcome = st.session_state["trends"][-2]["Prediction"]
        actual = outcomes[-1]
        if previous_outcome != actual:  # Incorrect prediction
            st.session_state["loss_count"] += 1
        else:
            st.session_state["loss_count"] = 0  # Reset on correct prediction

    # Display counts
    st.write(f"Big Count: {big_count}, Small Count: {small_count}")

# Footer
st.info("This tool predicts the next outcome based on saved trends and adapts to minimize losses.")
