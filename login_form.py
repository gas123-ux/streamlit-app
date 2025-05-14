import streamlit as st
def app():	
	st.title("Login")
	username = st.text_input("Username:")
	password = st.text_input("Password:")
	userlist = ["dog123","cat123","iworkhere5678"]
	passlist = ["Ilikeweiners","catfoodtastesgood","IdOnTwOrKhErE"]
	userpassword = dict(zip(userlist,passlist))
	if st.button("Login"):
		if username not in userlist:
			st.warning("This username doesn't exist.")
		else:
			if password == userpassword[username]:
				st.success("You're logged in!")
			else:
				st.warning("Incorrect password. Please try again.")