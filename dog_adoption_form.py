import streamlit as st
def app():
	title = st.title("Dog Adoption Form")
	name = st.text_input("Full Name: ")
	gender = st.radio("Gender",["M","F","Other"])
	age = st.radio("Age",[18,19,20,21,'21+'])
	marriage = st.multiselect("Marital Status",["Married","Engaged","Dating","Single","Divorced","Widowed"])
	address = st.text_input("Address")
	email = st.text_input("Email Address")
	phone = st.text_input("Phone Number")
	ai = st.selectbox("Adoption Info",["Shelter","Breeder","Other"])
	breed = st.text_input("Dog Breed")
	dogname = st.text_input("Name of Dog")
	chip = st.radio("Microchip?",["Yes","No"])
	pets = st.radio("Any other pets?",["Yes","No"])
	check = st.checkbox("I agree to be sent promotional emails and messages for food, toys and more.")
	if st.button('Submit'):
		if name == "":
			st.warning("Enter your name.")
		if marriage == "":
			st.warning("Select marital status.")
		if address == "":
			st.warning("Enter your address. Dox yourself.")
		if phone == "":
			st.warning("Phone number missing.")
		if breed == "":
			st.warning("Breed is missing.")
		if dogname == "":
			st.warning("Dog's name is missing.")
		else:
			st.success("Your form has been submitted successfully. Have a good day and get off this tab :)")
