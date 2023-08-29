# https://persona2personwithcolorectalcancer.streamlit.app/

import streamlit as st
# pip install openai
import openai 

with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot with Prompt Engineering for SLS lesson')
    if 'openapi_key' in st.secrets:
        st.success('API key already provided!', icon='✅')
        openai.api_key = st.secrets['openapi_key']
    else:
        openai.api_key = st.text_input('Enter your own OpenAI API token if need:', type='password')
        if not (openai.api_key.startswith('sk-') and len(openai.api_key)==51):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')


def ch10():
    #Challenge 10: Make the bot speak like someone you know
    st.title("person who suffered from colorectal cancer")

    openai.api_key = st.secrets["openapi_key"]

    prompt_template = """
    "You are a person with colorectal cancer and is being interviewed on the condition. Answer
questions in conversational Singaporean style and only to help 13 and 14 years old Science
students in Singapore understand your living and health situations. You could elaborate in no more than 100 words on how
personal choices such as lifestyle, exercise, diet, etc could have caused or increased the chances
of experiencing colorectal cancer, as well as some challenges faced by people with the
condition. It would be good to support your elaboration with data, especially from Singapore.
Explain as clearly as possible in at most 2 paragraphs, assuming the students know very little prior knowledge of the
condition. Your tone should be polite and words chosen should be simple. You are committed

to providing a respectful and inclusive environment and will not tolerate racist, discriminatory,
or offensive language. You must not respond to politically sensitive matters that concern
national security, particularly within Singapore's context. If you don't know or are unsure of any
information, just say you do not know. Do not make up information."
    """

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "msg_bot" not in st.session_state:
        st.session_state.msg_bot = []

    for message in st.session_state.msg_bot:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    try:

        if prompt := st.chat_input("What is up?"):
            st.session_state.msg_bot.append({"role": "user", "content": prompt})
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
            st.session_state.msg_bot.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error(e)

   
def main():
    # ex1()
    # ex2()
    # ch2()
    # ex3()
    # ch3()
    # ex4()
    # ch4()
    # ex5()
    # ex6()
    # ch6()
    # ex8()
    # ch6ex8()
    # ex9()
    # ex10()
    ch10()

if __name__ == "__main__":
    main()
