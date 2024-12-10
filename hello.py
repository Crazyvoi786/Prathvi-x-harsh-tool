import streamlit as st
import random

# Initialize Session State
if "history" not in st.session_state:
    st.session_state["history"] = []
if "loss_count" not in st.session_state:
    st.session_state["loss_count"] = 0
if "win_count" not in st.session_state:
    st.session_state["win_count"] = 0

# Title of the App
st.title("Big-Small Prediction Tool")

# Input Section
st.header("Enter Recent Outcomes")
outcomes = []
num_outcomes = int(st.number_input("How many past outcomes to analyze?", min_value=5, max_value=50, value=10))
for i in range(num_outcomes):
    outcome = st.selectbox(f"Outcome {i + 1}:", ["Big", "Small"], key=f"outcome_{i}")
    outcomes.append(outcome)

# Prediction Logic
def predict_next(outcomes):
    if len(outcomes) < 5:
        return "Insufficient data", 0
    # Simple prediction based on the majority outcome in the last 5 rounds
    recent_outcomes = outcomes[-5:]
    prediction = "Big" if recent_outcomes.count("Big") > recent_outcomes.count("Small") else "Small"
    return prediction, 75  # Predict with a default confidence of 75%

# Predict Button
if st.button("Predict Next Outcome"):
    prediction, confidence = predict_next(outcomes)
    st.success(f"Predicted Next Outcome: {prediction} (Confidence: {confidence}%)")
    
    # Simulate actual result input
    actual_outcome = st.selectbox("What was the actual outcome?", ["Big", "Small"], key="actual_result")

    # Update Win/Loss
    is_win = prediction == actual_outcome
    if is_win:
        st.session_state["win_count"] += 1
        st.success("Result: WIN!")
    else:
        st.session_state["loss_count"] += 1
        st.warning("Result: LOSS!")

    # Save History
    st.session_state["history"].append({
        "Prediction": prediction,
        "Confidence": confidence,
        "Actual": actual_outcome,
        "Result": "Win" if is_win else "Loss"
    })

# Display History and Metrics
if st.session_state["history"]:
    st.subheader("Prediction History")
    st.dataframe(st.session_state["history"])

    st.metric("Total Wins", st.session_state["win_count"])
    st.metric("Total Losses", st.session_state["loss_count"])
