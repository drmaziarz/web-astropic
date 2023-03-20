import requests
import streamlit as st

api_key = "MdNhvgmjSdD7xZaeuIiTJVQMAJSp7WZL7bvSAADf"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
content = request.json()

about_pic = content["explanation"]
media_type = content["media_type"]
media = content["url"]
date = content["date"]
title = content["title"]
copyright = content["copyright"]

st.set_page_config(page_title="AstroPic",
                   page_icon="🌟",
                   layout="centered")

st.title("AstroPic")
st.subheader("Astronomy picture of the day")
st.write()
st.subheader(date)
st.header(title)
if media_type == "video":
    st.video(media)
else:
    st.image(media, caption="caption here")
st.info(about_pic)
st.write(f"Copyright: {copyright}")
