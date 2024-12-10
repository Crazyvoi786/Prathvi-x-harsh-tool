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
    last_outcome = outcomes[-1]  # Most recent outcome

    # Prediction Logic
    if big_count > small_count:
        prediction = "Small"  # Opposite of majority
    elif small_count > big_count:
        prediction = "Big"  # Opposite of majority
    else:
        # Tie case: Flip the last outcome
        prediction = "Small" if last_outcome == "Big" else "Big"

    # Display Prediction
    st.success(f"The Predicted Next Outcome is: {prediction}")

# Footer
st.info("This tool predicts the next outcome based on the trend of the last 5 results.")
