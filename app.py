import streamlit as st
import openai
import os

# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.set_page_config(page_title="Health Info Assistant", layout="centered")
st.title("🩺 Personalized Health Explanation Generator")

# Input fields
condition = st.text_input("Enter a medical condition (e.g., hypertension, diabetes):")
literacy_level = st.selectbox("Select health literacy level:", ["Beginner", "Intermediate", "Advanced"])
emotional_tone = st.selectbox("Select emotional tone:", ["Calm", "Neutral", "Empathetic"])
language = st.selectbox("Preferred language:", ["English", "Hindi", "Tamil", "Spanish"])

# Button
if st.button("Generate Explanation"):
    with st.spinner("Generating explanation..."):
        # Prompt template
        prompt = f"""
You are a helpful and clear healthcare assistant.
Explain the following medical condition to a patient: {condition}.
Use language appropriate for someone with {literacy_level.lower()} health knowledge.
Be {emotional_tone.lower()} in your tone.
Speak in {language}.
Keep it short and easy to understand.
"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a medical assistant who gives empathetic, simple, and accurate responses."},
                    {"role": "user", "content": prompt}
                ]
            )
            answer = response['choices'][0]['message']['content']
            st.markdown("### 📝 Explanation")
            st.success(answer)

        except Exception as e:
            st.error(f"Error: {e}")
