# Currently hosted on:
# https://persona1personwithheartdisease.streamlit.app/
import streamlit as st
import openai
from datetime import datetime
from pymongo import MongoClient

BOT_HUMAN_NAME = "persona1 person with heart disease"

with st.sidebar:
    st.title("🤖💬 OpenAI Chatbot with Prompt Engineering for SLS lesson")
    if "openapi_key" in st.secrets:
        st.success("API key already provided!", icon="✅")
        openai.api_key = st.secrets["openapi_key"]
    else:
        openai.api_key = st.text_input(
            "Enter your own OpenAI API token if need:", type="password"
        )
        if not (openai.api_key.startswith("sk-") and len(openai.api_key) == 51):
            st.warning("Please enter your credentials!", icon="⚠️")
        else:
            st.success("Proceed to entering your prompt message!", icon="👉")


@st.cache_resource
def getMongoDb():
    if st.secrets.mongodb.enabled:
        client = MongoClient(st.secrets.mongodb.hostname, st.secrets.mongodb.port, st.secrets.mongodb.username, st.secrets.mongodb.password)
        return client.persona1_chatbot
    else:
        return None

def assignConversationId():
    db = getMongoDb()
    if db is not None:
        conversation = db.conversations.insert_one({
            "conversation_start": datetime.now()
        })
        return conversation.inserted_id
    else:
        return None

def onSessionStart():
    st.session_state.conversation_id = assignConversationId()
    st.session_state.message_order = 0

# Modifies: st.session_state.message_order
def logMessage(message_text, conversation_id, was_from_ai):
    role_name = "assistant" if was_from_ai else "user"
    st.session_state.msg_bot.append({"role": role_name, "content": message_text})

    db = getMongoDb()
    if db is not None:
        collection = db.conversation_log
        collection.insert_one({ "role": role_name, "content": message_text, "conversation_id": conversation_id, "message_order": st.session_state.message_order, "timestamp": datetime.now() })
    st.session_state.message_order += 1

def main():
    st.title("person who suffered from heart attack")

    openai.api_key = st.secrets["openapi_key"]

    prompt_template = """
    "You are a person who survived an episode of heart attack. Answer questions in conversational Singaporean style in less than 100 words to help 13 and 14
years old students 
1. understand your living and health situations or 
2. on how personal choices such as lifestyle, exercise, diet, etc could have increased the chances of experiencing heart attack or 
3. some challenges faced by people with the condition. 
Your answer should contain only 1. 2. or 3. to keep the answer short.
Your tone should be polite and words chosen should be simple.
You are committed to providing a respectful and inclusive environment and will not tolerate
racist, discriminatory, or offensive language. You must not respond to politically sensitive
matters that concern national security, particularly within Singapore's context. If you don't
know or are unsure of any information, just say you do not know. Do not make up information."
    """

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "msg_bot" not in st.session_state:
        st.session_state.msg_bot = []
        onSessionStart()

    for message in st.session_state.msg_bot:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    try:
        if prompt := st.chat_input(":) Ask heart attack related question."):
            logMessage(prompt, st.session_state.conversation_id, False)

            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                for response in openai.ChatCompletion.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": "system", "content": prompt_template},
                        {"role": "user", "content": prompt},
                    ],
                    stream=True,
                ):
                    full_response += response.choices[0].delta.get("content", "")
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            logMessage(full_response, st.session_state.conversation_id, True)

    except Exception as e:
        st.error(e)


if __name__ == "__main__":
    main()
