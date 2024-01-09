import streamlit as st 
from PIL import Image 
st.header('''"Confused by Market Trends? Ask, Learn, and Navigate Together!“
''')
st.markdown('<style>div.block-container{padding-top:2rem}</style>',unsafe_allow_html=True)
st.markdown('''"Market Minds Unite: A Hub for Traders, Investors, and Inquisitive Minds! Join the pulse of an engaging community where traders and investors from all walks of life come together. This is more than just a forum; it's a collaborative space for sharing experiences, seeking advice, and fostering a collective spirit of growth. Your go-to destination for connecting with like-minded individuals, exploring diverse perspectives, and unleashing the power of collective wisdom."
''')
image=Image.open(r"C:\Users\Windows 11\OneDrive\Desktop\community.jpg")
st.image(image)