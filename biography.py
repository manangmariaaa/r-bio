import streamlit as st
import PIL as image
from datetime import datetime

st.title("My Biography")

st.header("Full Name")
name = st.text_input("Name", "Marialyn Ramada")
birtday = st.text_input ("Birthday","April 4, 2006" )
today = datetime.datetime.today()
birth_date = datetime.strptime(birthday, "%B %d, %Y")
age = today.year - birth_date.year - ((today.month, today.day)<(birth_date.month, birth_date.day))
st.write (f" Age: {age}")
gender = st.selectbox ("Gender", ["Female", "Male","Prefer not to say"])

st.header ("Contact Information")
contact= st.text_input("Cellphone Number", "09387610532")
contact= st.text_input("Facebook", "Maria Ramada")
contact= st.text_input("Gmail Account", "ramadamarialyn@gmail.com")

st.header ("Educational Attainment")
elememtary = st.text_input("Elementary", "Albor Central Elementary School")
High_School= st.text_input("High School", "Albor National High School")
College = st.text_input("College", "Surigao del Norte State University")

st.header("Parental Information")
father = st.text_input("Father's Full name", "Joven Ramada")
mother = st.text_input ("Mother's Full name", "Marife Ramada")
contact= st.text_input("Father's Cellphone Number", "09318327654")
birthday = st.text_input ("Father's Birthday", "December 07 1970")
birthday = st.text_input ("Mother's Birthday", "August 03 1973")
contact = st.text_input("Mother's Cellphone Number", "09815944921")