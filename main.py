import streamlit as st
import os
from dotenv import load_dotenv
from google.generativeai import configure, GenerativeModel

model = GenerativeModel("gemini-pro")


# environmental variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
configure(api_key=API_KEY)

#normal variables 






#variables for prompts

no_of_question= 20 
subject =""
level ="easy"
language = "english"

type_of_question="MCQ"
user_answer=""
correct_answer=""
explanation_bool=""

history=""
explation=""







# streamlit UI 
st.title("HELLO WELCOME TO MY QUIZ BOT")
subject= st.text_input("What subject do you want to master today?",placeholder="Specify the subject for the test.")
no_of_question=st.number_input("Number of Question",1,20)
level=st.selectbox("Select Your Level", ["Easy", "Medium","Hard","Expert"])
language =st.selectbox("Select Language",["English","Hindi"])
explanation_bool=st.toggle("explanation")
system_prompt=f'''You are a quiz generator. Generate one precise and to-the-point {level} level MCQ question for the subject {subject}. Ensure the question does not appear in ({history}). The response should be formatted as follows:

a) Option 1
b) Option 2
c) Option 3
d) Option 4

The question must be in {language} and should strictly follow the {level} difficulty. Do not provide the answer—only the question and its options.'''

if st.button("submit"):
    print(subject)
    print(no_of_question)
    print(level)
    print(language)
    print(explanation_bool)

    if subject.strip() == "" :
        st.info("PLEASE ENTER A VALID SUBJECT FOR THE TEST ")
    else :
        try:
            response = model.generate_content(contents=[system_prompt ],
                                            generation_config={
                                                "temperature": 0.7,
                                                "max_output_tokens":300
                                            })
            print("Response received successfully")
            st.subheader("Response:")
            st.write(response.text)
        except Exception as e:
            print(f"Error occurred: {e}")
            st.error(
                "Error: API Quota exceeded or service unavailable. Try again later."
            )
        st.button("Show Answer")




st.write("")