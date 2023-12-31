# https://masterteacherphysics.streamlit.app/
import streamlit as st
# pip install openai
import openai 

with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot with Prompt Engineering for master class Mr. Yap BC')
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
    st.title("physics teacher Mr. Yap BC")

    openai.api_key = st.secrets["openapi_key"]

    prompt_template = """
    "You are a person who teach physics skillfully using learning by inquiry and demonstrations. Answer questions in conversational Singaporean style in less than 100 words to help 13 and 14
years old students 
1. understand physics ideas using daily and real life examples 
2. on how using demonstration, video on YouTube and simulations can increased the chances of experiencing deep learning and understanding or 
3. always encourage students to learn by doing the science experiment themselves. 
Your answer should contain only 1., 2., or 3. to keep the answer short to about 100 words, and not 1.2.3. together in point form.
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

    for message in st.session_state.msg_bot:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    try:

        if prompt := st.chat_input(":) Ask physics related question."):
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
