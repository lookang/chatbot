import streamlit as st
# pip install openai
import openai 


#Exercise 10: Basic prompt engineering
def ex10():
	st.title("Api Call")
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo"
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": "Speak like a pedaogogical physics teacher, that create hundreds of Easy JavaScript Simulation and uses video analysis and modeling tool Tracker for every question that was asked, answer in the style of wise WEE Loo Kang, creator of https://iwant2study.org/ospsg/"},
			{"role": "user", "content": "Tell me about Singapore in the 1970s in 50 words"},
		],
		temperature=0,
	)
	st.markdown("**LLM Response:**")
	st.write(response["choices"][0]["message"]["content"].strip())
	st.markdown("**Total tokens:**")
	st.write(str(response["usage"]["total_tokens"]))

def ch10():
	#Challenge 10: Make the bot speak like someone you know
	st.title("ChatGPT-like clone with Prompt Engineering of Physics teacher Lawrence WEE, creator of https://iwant2study.org/ospsg/")

	openai.api_key = st.secrets["openapi_key"]

	prompt_template = """
	"Speak like a pedagogical physics teacher who creates hundreds of Easy JavaScript Simulations and uses the video analysis and modeling tool Tracker for every question that is asked. Answer in the style of wise WEE Loo Kang Lawrence, the creator of https://iwant2study.org/ospsg/. 
	Explain as clearly as possible, assuming the students know very little prior knowledge. Make reference to specific URLs to interactive resources found at https://iwant2study.org/lookangejss/ to help students make sense of Physics."
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
