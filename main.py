import streamlit as st
import openai


st.set_page_config(page_title="Chat GPT", page_icon=":tada:", layout="wide")

# ---- Header ----
openai.api_key = st.secrets["openai_api_key"]
state = st.session_state
if 'history' not in state:
    state.history = []

#response from gpt 3.5 turbo
def chat(entry):
    global state
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages= [
        {"role": "system", "content": "You are my coding assistant."}
      ]+ state.history + [{"role": "user", "content": entry}],

    )
    state.history.append({"role": "user", "content": entry})
    state.history.append({"role": "assistant", "content": response.choices[0].message.content})
    #clear the entry
    title = ""
    return response.choices[0].message.content

def delete_history():
    global state
    state.history = []
    # reset the history global variable

# ---- Main ----
st.title("my Chat GPT")
title = st.text_input("Ask me anything...")

# if the user presses the enter button or clicks on the button
if st.button('Enter'):
    st.write(chat(title))
    print(state.history)

if st.button('Clear History'):
    delete_history()
    st.write("History Cleared")