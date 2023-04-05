import streamlit as st
import numpy as np
from selenium import webdriver
from random import randint
from time import sleep

# list21=['Harry Potter']

# link = '([harry potter](https://www.google.com/search?q=harry potter))'
# st.markdown(link, unsafe_allow_html=True)

# list21=['Harry Potter ','manngo','ms dhoni','dav']


import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])

    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title) 
    return recommended_movies

model=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(model)

similarity=pickle.load(open('similarity.pkl','rb'))

st.image('poster.jpg')
st.title('Movie Recommender System')

selected_movie_name=st.selectbox('Movies Name',movies['title'].values)

message_Check = False
domain=str('https://www.google.com/search?q=')
value = str('')
finalLink = str('')
#([harry potter](https://www.google.com/search?q=harry potter)
#domain=str('')
if st.button('Recommend'):
    recommendation=recommend(selected_movie_name)
    for i in recommendation:
        # st.write(i)
        value = i
        finalLink = "["+value+"]"+"("+domain+value.replace(" ", "") + ")"
        st.markdown(finalLink, unsafe_allow_html=True) 
        message_Check=True
        

if message_Check:
    st.success('Here! is the recommended movies for you')

# link = '[GitHub](http://github.com)'
# st.markdown(link, unsafe_allow_html=True) 

