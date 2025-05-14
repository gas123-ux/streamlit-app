import login_form
import dog_adoption_form
import streamlit as st

pages_dict = {
	"Login": login_form, 
	"Form": dog_adoption_form

} 
st.sidebar.title ("Navigation")
choices= st.sidebar.radio("Go To", tuple(pages_dict.keys()))
if choices == "Form":
	dog_adoption_form.app()
else:
	login_form.app()