# run_agent.py
import streamlit as st

# Initialize session state once
if "messages" not in st.session_state:
    st.session_state.messages = []

# Define skills
skills = {
    "greet": {
        "trigger": ["good morning", "good evening"],
        "response": "Hello! How can I help you today?"
    },
    "hello-world": {
        "trigger": ["hello"],
        "response": "Hello! How can I assist you today?"
    },
    "faq": {
        "trigger": ["price", "pricing", "cost"],
        "response": "Our products range from $50 to $500 depending on features. Do you want details on a specific product?"
    },
    "troubleshoot": {
        "trigger": ["issue", "problem", "error"],
        "response": "Can you describe the problem? Then I will provide a step-by-step solution."
    }
}

st.title("Customer Support Chatbot")
st.write("Type your message below. The agent will respond based on the workflow.")

# User input
user_input = st.text_input("You:", key="input")

if user_input:
    # Check triggers
    response = "Sorry, I don't understand. Can you rephrase?"
    for skill, data in skills.items():
        if any(trigger in user_input.lower() for trigger in data["trigger"]):
            response = data["response"]
            break

    # Save conversation
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Agent", response))

# Display conversation
for speaker, msg in st.session_state.messages:
    if speaker == "You":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Agent:** {msg}")