import streamlit as st
import pandas as pd
import numpy as nd
import streamlit as st
import pandas as pd 
import numpy as nd
import matplotlib.pyplot as plt
import plotly.express as px
import requests 

st.title("Hello, Streamlit")
st.write("this is my 1st streamlit :streamlit: ")
st.text("lets get started")

name = st.text_input("Enter your Name:")

if st.button("Greets!"):
    st.success(f"Hello {name} !* Sir")

df = pd.DataFrame(nd.random.randn(10,2), columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

st.video("https://youtu.be/_uzf1NwNVJ0?si=3XKaTzjSdBDEqFyj")

upload_file = st.file_uploader("upload a csv." , type="csv")
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.sidebar.title("Navigator")
st.sidebar.subheader("about")

st.number_input("Enter your marks", min_value=0, max_value=100)
st.slider("choose your rating",0,10)
st.text_area("Enter 300s word assay:")
st.markdown("I am **Bold**, i am *ittalic* , i am `code` , I am link, [YCCE](https://ycce.edu/)")

st.code("for i in range(5): print(i)", language="python")

st.selectbox("selelct your Grade", ["A", "B", "C"])
st.multiselect("selelct your Grade", ["Samosa", "Sweet", "Juice", "chhutti"])

st.checkbox("Agree to T&C")

option = st.radio("selelct your choice", ["A", "B", "C"], index=0)

if option == "A":
    st.write("1 day holiday alloted")
if option == "B":
    st.write("2 day holiday alloted")
if option == "C":
    st.write("Fail-very dangorous")

with st.form("login form"):
    username = st.text_input("Enter your UserName Here")
    password = st.text_input("Enter your Password Here")
    submitted = st.form_submit_button("Log in")

if submitted:
    st.success(f"welcome {username}!")

fig, ax = plt.subplots()
ax.plot([1,2,3],[1,4,9])
st.pyplot(fig)


df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig)
question = st.text_input("Ask Me Anything")

if st.button("Ask AI"):

    response = requests.post("http://localhost:11434/api/generate",
        json={
            "model": "gemma 2:2b",
            "prompt": question,
            "stream": False,
            "temperature": 0.7
            #"messages":[{"role": "user", "content": question}]
        }
    )

    answer = response.json()["response"]

    st.write(answer)
