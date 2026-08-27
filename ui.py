import streamlit as st
from youtube_analyzer import youtube_agent_analyzer

st.set_page_config(
    page_title="YoutubeAnalyzer",
    layout="centered"
)

st.title("🎥 AI Youtube Video Analzyer")

@st.cache_resource
def get_agent():
    return youtube_agent_analyzer()

agent=get_agent()

# input box

video=st.text_input("Enter Youtube Video Link")

button=st.button("Analyze Video")

if video and button:
    with st.spinner("Analyzing..."):
        response=agent.run(
            f"Analyze this video :{video}"
        )

    st.markdown("Analysis Report: ")
    st.markdown(response.content)