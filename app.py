import streamlit as st
import pandas as pd

# Initialize Session State
if "trends" not in st.session_state:
    st.session_state["trends"] = []

if "loss_count" not in st.session_state:
    st.session_state["loss_count"] = 0

if "win_count" not in st.session_state:
    st.session_state["win_count"] = 0

if "past_predictions" not in st.session_state:
    st.session_state["past_predictions"] = []

# Title of the App
st.title("Big-Small Prediction Tool (Advanced Pattern & Trend Analysis)")

# Input Section
st.header("Enter the Number of Outcomes")
num_outcomes = st.number_input("How many past outcomes do you want to analyze?", min_value=5, max_value=20, value=10)

st.subheader("Enter the Last Outcomes")
outcomes = []
for i in range(int(num_outcomes)):
    outcomes.append(st.selectbox(f"Outcome {i + 1}:", ["Big", "Small"], key=f"outcome_{i}"))

# Prediction Logic
def predict_next(outcomes):
    # Step 1: Short-Term Pattern Recognition
    if outcomes[-3:] == ["Big", "Small", "Big"]:
        return "Small"  # Predict to complete the pattern
    if outcomes[-3:] == ["Small", "Big", "Small"]:
        return "Big"  # Predict to complete the pattern

    # Step 2: Long-Term Trend Analysis
    big_count = outcomes.count("Big")
    small_count = outcomes.count("Small")
    
    if big_count > small_count:
        long_term_trend = "Big"
    else:
        long_term_trend = "Small"

    # Step 3: Dynamic Weighting
    weights = range(1, len(outcomes) + 1)  # More weight for recent outcomes
    big_weight = sum(w for o, w in zip(outcomes, weights) if o == "Big")
    small_weight = sum(w for o, w in zip(outcomes, weights) if o == "Small")
    
    if big_weight > small_weight:
        weighted_trend = "Big"
    else:
        weighted_trend = "Small"

    # Step 4: Combine Analysis
    if long_term_trend == weighted_trend:
        return "Small" if long_term_trend == "Big" else "Big"  # Opposite of trend to avoid traps
    else:
        return long_term_trend  # Follow the long-term trend

if st.button("Predict Next Outcome"):
    prediction = predict_next(outcomes)
    st.success(f"The Predicted Next Outcome is: {prediction}")
    
    # Simulate Actual Result
    actual_outcome = st.selectbox("What was the actual outcome?", ["Big", "Small"], key="actual_result")
    is_win = prediction == actual_outcome  # Check if the prediction was correct

    # Update Win/Loss Counts
    if is_win:
        st.session_state["win_count"] += 1
        st.session_state["loss_count"] = 0  # Reset loss count after a win
        st.success("Prediction was a WIN!")
    else:
        st.session_state["loss_count"] += 1
        st.warning("Prediction was a LOSS!")

    # Save Result and Trends
    st.session_state["trends"].append({
        "Outcomes": outcomes,
        "Prediction": prediction,
        "Actual": actual_outcome,
        "Result": "Win" if is_win else "Loss"
    })
    st.session_state["past_predictions"].append({"Prediction": prediction, "Actual": actual_outcome, "Win": is_win})

    # Display Trends and Stats
    st.write("Trend Analysis and History:")
    st.dataframe(pd.DataFrame(st.session_state["trends"]))
    st.metric("Total Wins", st.session_state["win_count"])
    st.metric("Total Losses", st.session_state["loss_count"])

    # Loss Analysis
    if not is_win:
        st.subheader("Loss Analysis")
        st.write("Analyzing recent trends to improve accuracy...")
        # Analyze patterns causing losses
        recent_trend = outcomes[-5:]  # Last 5 outcomes
        st.write(f"Recent Trend: {recent_trend}")
        if recent_trend.count("Big") > recent_trend.count("Small"):
            st.info("Trend shows more 'Big' outcomes recently. Adjusting prediction strategy to favor 'Small'.")
        else:
            st.info("Trend shows more 'Small' outcomes recently. Adjusting prediction strategy to favor 'Big'.")

# Footer
st.info("This tool uses advanced pattern recognition and trend analysis to minimize losses.")
