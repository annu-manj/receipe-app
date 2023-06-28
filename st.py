
import streamlit as st
import pickle


top_rated=pickle.load(open("b.pkl",'rb'))


st.header("Top_Rated_Recipe Recommendation System")
selectvalue=st.selectbox("Top_Rated_Recipe From DropDown",top_rated)  


