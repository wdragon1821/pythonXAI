import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]   #take out the OPENAI_API_KEY from the secrets.
ss = st.session_state
if "history" not in ss:     #initialize the history if it doesn't exist
    ss.history = []     #create an empty list to store the conversation history
if"system_message" not in ss:   #initialize the system message
    ss.system_message = (
        "請用繁體英文進行後續對話"   #if the system message doesn't exist, set it to a default message
    )
if"model" not in ss:    #initialize the model
    ss.model = "gpt-4o-mini"    #if the model doesn't exist, set it to a default model


#set the columns with the width of 4, 2, and 1
col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    ss.system_message = st.text_input("系統提示", ss.system_message)
with col2:
    ss.model = st.selectbox("AI模型",["gpt-4o-mini","gpt-4","gpt-4o-searcher-preview",],)
with col3:
    if st.button("🗑️") :    #make a butten to clear the history at column 3
        ss.history = []    #clear the history when the button is clicked
        st.rerun()  #rerun the app when the button is clicked

for message in ss.history:    #loop through the history and display the messages
    if message["role"] == "user":    #if the message is from the user
        st.chat_message("user", avatar="🪄").write(message["content"])    #display the message as a user message
    else:
        st.chat_message("assistant", avatar="✨").write(message["content"])    #display the message as an assistant message

prompt = st.chat_input("請輸入想對話的訊息")    #create a chat input for the user to input the message
if prompt:
    ss.history.append({"role": "user", "content":prompt})    #add the user message to the history

    response = openai.chat.completions.create(
        model=ss.model,    #use the model from the session state
        messages=[{"role": "system", "content": ss.system_message}] + ss.history,    #add the system message to the beginning of the history
    )

    assistant_message = response.choices[0].message.content    #get the assistant message from the response
    ss.history.append({"role": "assistant", "content": assistant_message})    #add the assistant message to the history
    st.rerun()    #rerun the app to display the new message