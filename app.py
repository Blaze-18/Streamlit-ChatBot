import streamlit as st
import time
from streamlit_option_menu import option_menu
import streamlit.components.v1 as com
from gen_text import generated


st.set_page_config(
    page_title="Echo Bot",  # Custom page title
    page_icon=":rocket:",   # Custom page icon 
)

#Custom css for background
page_bg_img = """
<style>
    [data-testid="stAppViewContainer"]{
        background: rgb(131,58,180);
        background: linear-gradient(90deg, rgba(131,58,180,1) 22%, rgba(253,29,29,1) 100%, rgba(252,176,69,1) 100%);
    }
    [data-testid="stHeader"] {
        display: none;
    }
 #fixed-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center; /* Center horizontally */
    width: 100%;
    background-color: rgba(0, 0, 0, 1); /* Black background with 80% opacity */
    z-index: 1000;
    padding: 5px; /* Adjust padding to reduce occupied space */
    text-align: center;
    color: white;
}
    .stApp {
        padding-top: 30px;  /* Adjust padding to ensure content is not hidden under the fixed header */
    }
    .loader {
        border: 4px solid #FFFFFF; /* Light grey */
        border-top: 4px solid #ff0000; /* RED */
        border-radius: 50%;
        width: 25px;
        height: 25px;
        animation: spin 1s linear infinite;
        margin: auto;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .centered-text {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 24px;
        color: white;
        z-index: 999;
        text-align: center;
    }
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Custom text with fixed position
st.markdown("<div id='fixed-header'><h2>Welcome to the Echo Bot</h2></div>", unsafe_allow_html=True)

if "question_asked" not in st.session_state:
    st.session_state.question_asked = False

if not st.session_state.question_asked:
    st.markdown("<div class='centered-text'>Ask me anything!</div>", unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up ?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.question_asked = True  # Mark that a question has been asked

    # Placeholder for the assistant's response
    response_placeholder = st.empty()

    # Display loading animation
    with response_placeholder.container():
        st.markdown('<div class="loader"></div>', unsafe_allow_html=True)

    time.sleep(0.7)

    
    response_placeholder.empty() 
    response = f"{prompt}"
    
    #response = generated(prompt) ***Here goes your custom response***
    
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": prompt})
    
    st.experimental_rerun()
