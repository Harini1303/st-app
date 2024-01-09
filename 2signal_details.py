import streamlit as st 
from PIL import Image
st.header('''"Market Mastery Signals: Precision for Daily Success"''')
st.markdown('<style>div.block-container{padding-top:2rem}</style>',unsafe_allow_html=True)
st.markdown('''"Embark on a journey of daily success with Market Mastery Signals – your precision guide in market maneuvers. Fueled by efficient research based algorithm, advanced analytics, these signals provide strategic insights for making informed decisions at each market day/close(TBD). Whether locking in gains or planning for the future, let Market Mastery Signals be your key to crafting success with unwavering precision every day."
''')
image=Image.open(r"C:\Users\Windows 11\OneDrive\Desktop\signal.jpg")
st.image(image)