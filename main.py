import preprocessed_outputs as out
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
import streamlit as st
from langchain_openai import OpenAI
load_dotenv()
with open('./style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


prompt_template = PromptTemplate(
    template='''I want to learn  {concept} in {days}
    If the entered topic is not an actual learning topic or it is a random question like who made you, or anything not related to learning, return Sorry please enter valid input.
    Give me a roadmap to learn this. It should be in group of 5 days. Do not have any text before it. Do not use more than 300 words total while answering. Thats an order. write very concise points.
    See this example on how to write it 
    Day 1-5: leave a line
    1.
    2.

    Day 6-10: leave a line
    1.
    2. 
    etc
    Format it nicely with ample spacing.
    ''',
    input_variables=['concept','days']
)

st.title(":world_map: Roadmap")

col1, col2 = st.columns(2)
with col1:
    user_prompt = st.text_input("Enter what you want to learn :rocket:",max_chars=20)
with col2:
    no_of_days = st.selectbox(
    'Select number of days to learn :date:  ',
    ('10 days', '15 days', '20 days','30 days'))

apikey = st.text_input("Enter your OpenAI API key :key: ",type='password')
generate_with_openai = st.button('Generate using API Key',type='secondary')
st.write("Don't have an OpenAI API Key? Dont worry, you can still test it out! 	:arrow_down:")
option = st.selectbox(
    'Select from preprocessed Roadmaps :zap: ',
    ('Javascript-30days', 'swimming-30days', 'Pandas-15days','Python-20days','boxing-30days','Standup Comedy-15days'))
preprocessed_output = st.button('Generate without API Key',type='primary')


if generate_with_openai and user_prompt and apikey:
    with st.spinner('Generating...'):
        llm = OpenAI(openai_api_key=apikey,temperature=0.6,model="gpt-3.5-turbo-instruct",max_tokens=1000)
        output = llm(prompt_template.format(concept=user_prompt,days=no_of_days))
        st.write(output)

if preprocessed_output and option:
    if option == "Javascript-30days":
        st.write(out.preout_JS30)
    elif option == "swimming-30days":
        st.write(out.preout_swimming30)
    elif option == "Pandas-15days":
        st.write(out.preout_pandas15)
    elif option == "Python-20days":
        st.write(out.preout_python20)
    elif option == "boxing-30days":
        st.write(out.preout_boxing30)
    else:
        st.write(out.preout_standupcomedy15)

