import streamlit as st
from core import init_query_agent

st.set_page_config(page_title="Movie AI Agent", page_icon="🎬")

st.title("Movie AI Agent 🎬")

@st.cache_resource
def load_agent():
    return init_query_agent()

agent = load_agent()

question = st.text_input("Въпрос:")

if question:
    with st.spinner("Мисля..."):
        response = agent.ask(question)
        st.write(response)
