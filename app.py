import streamlit as st #for ui
import os
from dotenv import load_dotenv #to get env variables loaded into the application
load_dotenv() #loading of all the env variable

import google.generativeai as genai
history=[]

#genai config of api
# os.environ['GOOGLE_API_KEY'] = 'AIzaSyBPQF0g5EfEPzEiGRzA3iNzJZK4jDukMvE'
genai.configure(api_key='AIzaSyBPQF0g5EfEPzEiGRzA3iNzJZK4jDukMvE')
# initialise the model
model = genai.GenerativeModel('gemini-pro')

# define a function to generate response from llm
def get_gemini_response(ques):
    resp = model.generate_content(ques)
    return resp.text

# setting up streamlit app
st.set_page_config(
    page_title="Gemini pro Q/A project",
    layout="wide",
    initial_sidebar_state="expanded",
)

# setting up header
st.header("Gemini Q/A app")
# st.title

question = st.text_input("Ask a question: ")


if st.button("Submit"):
    response = get_gemini_response(question)
    st.write("User:", question)
    st.write("Bot:", response)
    history.append((question, response))


st.sidebar.title("Chat History")
for i, (user_q, bot_resp) in enumerate(history[::-1], start=1):
    st.sidebar.write(f"{i}. User: {user_q}")
    st.sidebar.write(f"   Bot: {bot_resp}")