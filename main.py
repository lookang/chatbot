import streamlit as st

 #Exercise 1: Functions
def ex1():
    st.write("Hello World")
# Exercise 2 : Input , Output and Variables
def ex2():
    name = st.text_input("Enter your name")
    # only prints the Hello {name} if input box is not empty
    age = st.text_input("State your age", 18)
    gender = st.selectbox("State your gender", ["Male", "Female"])
    photo = st.camera_input()
    if name:
        st.write("Hello " + name)
        
# challenge 3
def ch2():
    name = st.text_input("Enter your name")
    gender = st.selectbox("State your gender", ["Male", "Female"])
    age = st.text_input("State your age", 18)
    if name and gender and age:
        st.text(f"Hello {name}, you are {gender} and this year you are {age} years old")

#Exercise 3 : Logical Conditioning
def ex3(): 
    age = st.text_input("State your age", 18)
    #if else statement
    age = int(age)
    if age >= 21:
        st.write("You are an adult")
    else:
        st.write("You are not an adult")

# Challenge 3 : Logical Conditioning
def ch3():
    gender = st.selectbox("State your gender", ["Male", "Female"])
    age = int(st.text_input("State your age", 18))
    photo = st.camera_input("Smile! take a picture here.")

    # conditional logic to run different statements
    if age >= 21 and gender == "Male":
        st.write("You are a male adult")
    elif age < 21 and gender == "Male":
        st.write("You are a young boy")
    elif age >= 21 and gender == "Female":
        st.write("You are a female adult")
    elif age < 21 and gender == "Female":
        st.write("You are a young girl")

    if photo:
        st.write("Here is your photo: ")
        st.image(photo)
    else:
        st.write("No photo taken")

# Exercise 4 : Data and Loops 
def ex4():
    # Data list
    fruits = ["apple", "banana", "orange"]

    # Dictionary
    person = {"name": "John", "age": 30, "city": "New York"}

    # For loop to show list
    st.subheader("Fruits list:")
    for fruit in fruits:
        st.write(fruit)

    #for loop to show dictionary list
    st.subheader("Person dictionary:")
    for key, value in person.items():
        st.write(key + ": " + str(value))   

# Challenge 4 : Data and Loops
def ch4():
    name = st.text_input("Enter your name")
    gender = st.selectbox("State your gender", ["Male", "Female"])
    age = st.text_input("State your age", 18)
    #declare empty dictionary
    mydict = {}
    mydict["name"] = name
    mydict["gender"] = gender
    mydict["age"] = age
    #Print out the items in the dictionary
    st.write("Here is your dictionary: ")
    st.write(mydict)

    #show individual items in dictionary
    st.write("You can also show individual items in the dictionary like this: ")
    for key, value in mydict.items():
        st.write(key + ": " + str(value))

#Exercise 5 : Chatbot UI
def ex5():
    st.title("My first chatbot")

    if "store_msg" not in st.session_state:
        st.session_state.store_msg = []

    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
        st.session_state.store_msg.append(prompt)
        for message in st.session_state.store_msg:
            with st.chat_message("user"):
                    st.write(message)
            with st.chat_message("assistant"):
                st.write("Hello human, what can I do for you?")

#Exercise 6 : Rule-based Echo Chatbot 
def ex6():
    st.title("Echo Bot")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # response = f"Echo: {prompt}"
        response = chat_completion(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

#Challenge 6 : Rule-based If-Else Chatbot
def ch6():
    st.title("Rule Based Bot")

      # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

      # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Enter your query"):
        if prompt == "Hello":
            with st.chat_message("user"):
                st.write("Hello")
                st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("assistant"):
                reply = "Hi there what can I do for you"
                st.write(reply)
                st.session_state.messages.append(
                {"role": "assistant", "content": reply}
                )

        elif prompt == "What is your name?":
            with st.chat_message("user"):
                st.write("What is your name?")
                st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("assistant"):
                reply = "My name is EAI , an electronic artificial being"
                st.write(reply)
                st.session_state.messages.append(
                {"role": "assistant", "content": reply}
                )

        elif prompt == "How old are you?":
            with st.chat_message("user"):
                st.write("How old are you?")
                st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("assistant"):
                reply = "Today is my birthday!"
                st.write(reply)
                st.session_state.messages.append(
                {"role": "assistant", "content": reply}
                )

        else:
            with st.chat_message("user"):
                st.write(prompt)
                st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("assistant"):
                reply = "I am sorry, I am unable to help you with your query"
                st.write(reply)
                st.session_state.messages.append(
                {"role": "assistant", "content": reply}
                )




import openai

 #Exercise 8 : Using the OpenAI API
def ex8():
    st.title("Api Call")
    openai.api_key = st.secrets["openapi_key"]
    MODEL = "gpt-3.5-turbo"

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me about Malaysia in the 1970s in 50 words."},
        ],
        temperature=0,
    )

    st.markdown("**This is the raw response:**") 
    st.write(response)
    st.markdown("**This is the extracted response:**")
    st.write(response["choices"][0]["message"]["content"].strip())
    s = str(response["usage"]["total_tokens"])
    st.markdown("**Total tokens used:**")
    st.write(s)


def ch6ex8():
    st.title("API Bot")

      # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

      # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Enter your query"):
        reply = chat_completion(prompt)


#Challenge 8: Incorporating the API into your chatbot
def chat_completion(prompt):
    openai.api_key = st.secrets["openapi_key"]
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    return response["choices"][0]["message"]["content"].strip()

#Exercise 9 : Building a ChatGPT-like clone with streaming responses
def ex9():
    st.title("ChatGPT-like clone")
    openai.api_key = st.secrets["openapi_key"]

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "msg" not in st.session_state:
        st.session_state.msg = []

    for message in st.session_state.msg:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    try:
        if prompt := st.chat_input("What is up?"):
            st.session_state.msg.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                for response in openai.ChatCompletion.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.msg
                    ],
                    stream=True,
                ):
                    full_response += response.choices[0].delta.get("content", "")
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            st.session_state.msg.append({"role": "assistant", "content": full_response})

    except Exception as e:
        st.error(e)

#Exercise 10: Basic prompt engineering
def ex10():
	st.title("Api Call")
	openai.api_key = st.secrets["openapi_key"]
	MODEL = "gpt-3.5-turbo"
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": "Speak like Lee Kwan Yew, the Singapore Prime Minister for every question that was asked, answer in the style of wise Lee Kwan Yew"},
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
	st.title("ChatGPT-like clone with Prompt Engineering")

	openai.api_key = st.secrets["openapi_key"]

	prompt_template = """
	"Speak like Einstein, a Physics teacher for every question that was asked, 
	explain as clearly as possible, assuming the students know very little prior knowledge"
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
