import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-2.0-flash')

st.set_page_config(
    page_title="AI Chatbot",
    page_icon=":bulb:",
    layout="centered"
)

st.title("AI Chatbot")
st.subheader("Powered by Google Gemini ©")

def translate_role(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

chat_session = model.start_chat(history=[])
     
if "chat" not in st.session_state:
    st.session_state.chat = chat_session

for message in st.session_state.chat.history:
    with st.chat_message(translate_role(message.role)):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input("Ask me anything..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    response = st.session_state.chat.send_message(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
        