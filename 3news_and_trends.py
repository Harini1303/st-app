import streamlit as st
from PIL import Image 
st.header("CHARTING THE MARKET RHYTHM")
st.markdown('''"Unveiling the day's market journey in a dynamic blend of graphs, videos, and text – where each moment tells a story of potential..!"''')
st.markdown('<style>div.block-container{padding-top:2rem}</style>',unsafe_allow_html=True)
col1,col2,col3=st.columns((3))
with col1:
    image=Image.open(r"C:\Users\Windows 11\OneDrive\Desktop\news3.jpg")
    st.image(image)
with col2:
    image=Image.open(r"C:\Users\Windows 11\OneDrive\Desktop\news2.jpg")
    st.image(image)
with col3:
    image=Image.open(r"C:\Users\Windows 11\OneDrive\Desktop\news1.jpg")
    st.image(image)