from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
import glob
import plotly.express as px

st.title("Diary Tone")

analyzer = SentimentIntensityAnalyzer()


filepaths = sorted(glob.glob("diary/*.txt"))
date = [name.strip(".txt").strip("diary/") for name in filepaths]
score_list = []
for filepath in filepaths:
    with open(filepath, 'r') as file:
        text = file.read()
        scores = analyzer.polarity_scores(text)
        score_list.append(scores)

positive_list = []
for score in score_list:
    positive_list.append(score["pos"])

st.subheader("Positivity")
figure = px.line(x=date, y=positive_list, labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(figure)

negative_list = []
for score in score_list:
    negative_list.append(score["neg"])

st.subheader("Negativity")
figure = px.line(x=date, y=negative_list, labels={"x": "Dates", "y": "Negativity"})
st.plotly_chart(figure)
