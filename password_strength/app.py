import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$, etc.).")

    return score, feedback

def get_strength_label(score):
    if score <= 1:
        return "Very Weak", "red"
    elif score == 2:
        return "Weak", "orange"
    elif score == 3:
        return "Moderate", "yellow"
    elif score == 4:
        return "Strong", "lightgreen"
    else:
        return "Very Strong", "green"

# Streamlit App
st.set_page_config(page_title="Password Strength Meter", layout="centered")

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)
    label, color = get_strength_label(score)

    st.markdown(f"**Strength: <span style='color:{color}'>{label}</span>**", unsafe_allow_html=True)

    st.progress(score / 5)

    if feedback:
        st.subheader("Suggestions:")
        for item in feedback:
            st.write(f"- {item}")
else:
    st.info("Please enter a password to check its strength.")
