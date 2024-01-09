import streamlit as st
from PIL import Image 
cl1,cl2,cl3=st.columns((3))
with cl2:
    image=Image.open(r"C:\Users\Windows 11\OneDrive\Desktop\user2.png")
    st.image(image)
    st.header('USER DETAILS')