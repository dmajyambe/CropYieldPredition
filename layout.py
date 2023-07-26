import streamlit as st

st.title("Registration form")
first, last = st.columns(2)
first_name = first.text_input('First name')
last_name = last.text_input("Last name")

email,mob=st.columns([3,1])
email.text_input('Email id')
mob.text_input("Tel")

user,pw,pw2=st.columns(3)
user.text_input("Username")
pw.text_input("Password",type="password")
pw2.text_input("Retype your password",type="password")

ch,bl,sub=st.columns(3)
ch.checkbox("I Agree")
sub.button('Submit')
