import streamlit as st 
import pandas as pd
import plotly.express as px

st.set_page_config('Tools and Features')
st.title('Tools and Features')
st.markdown('<style>div.block-container{padding-top:1rem}</style>',unsafe_allow_html=True)
df=pd.read_csv(r"C:\Users\Windows 11\Downloads\nse_data.csv")
#st.write(df['CATEGORY'].value_counts())
#st.write('hii')

#calculating volatility factor
volatility=[]
for index,row in df.iterrows():
        if int(row['HIGH_PRICE'])-int(row['LOW_PRICE'])==0:
            vol=0
        else:
            vol=int(row['CLOSE_PRICE'])-int(row['OPEN_PRICE'])/(int(row['HIGH_PRICE'])-int(row['LOW_PRICE']))
        volatility.append(vol)
df['VOLATILITY']=volatility


start_date=pd.to_datetime(df['DATE'].min())
end_date=pd.to_datetime(df['DATE'].max())
col1,col2=st.columns((2))
with col1:
    date1=pd.to_datetime(st.date_input("start date:",start_date))
with col2:
    date2=pd.to_datetime(st.date_input('end date',end_date))
df=df[(pd.to_datetime(df['DATE'])>=date1) & (pd.to_datetime(df['DATE'])<=date2)].copy()

st.sidebar.header('PICK YOUR FILTER')
#creating category wise dataframe
categories=st.sidebar.multiselect('Pick the categories of stock:',df['CATEGORY'].unique())
if categories:
    df_category=df[df['CATEGORY'].isin(categories)]
    
else:
    df_category=df.copy()
#creating industrywise dataframe
industries=st.sidebar.multiselect("Pick the industry of the stock",['1','2','3'])

#creating stock wise dataframe in timeframe
stocks=st.sidebar.multiselect('pick the desired stocks:',df_category['SECURITY'].unique())
if stocks:
    df_stocks=df[df['SECURITY'].isin(stocks)]
else:
    df_stocks=df_category.copy()
if not categories and not stocks:
    st.write("please select a filter")
    df_filtered=df
if categories and not stocks:
    df_filtered=df_category
elif stocks and not categories:
    df_filtered=df_stocks
elif stocks and categories:
    df_filtered=df_category[df_category['SECURITY'].isin(stocks)]

    
#st.subheader('VISUALISATIONS')
securities=df_filtered['SECURITY'].unique()
#st.write(securities)



#st.write(df_filtered.head())
st.markdown('''<style>
            .big-font{font-size:30px}
            </style>''',unsafe_allow_html=True)
st.markdown('''<style>
            .sub-font{font-size:20px}
            </style>''',unsafe_allow_html=True)
st.markdown('''<p class="big-font">VISUALISATIONS</p>''',unsafe_allow_html=True)
if stocks:
    for security in securities:
        st.markdown(f'''<p class="sub-font">COMPARISIONS OF PRICES OF {security} </p>''',unsafe_allow_html=True)
        df_security=df_filtered[df_filtered['SECURITY']==security]
        #st.write(df_filtered.head())
        fig=px.line(df_security,x='DATE',y=['OPEN_PRICE','CLOSE_PRICE','HIGH_PRICE','LOW_PRICE'],labels={'DATE':'DATE','value':'OHLC'})
        #fig.add_scatter(x=df_security['DATE'],y=df_security['CLOSE_PRICE'])
        #fig.add_scatter(x=df_security['DATE'],y=df_security['HIGH_PRICE'])
        #fig.add_scatter(x=df_security['DATE'],y=df_security['LOW_PRICE'])
        st.plotly_chart(fig,use_container_width=True)

        st.markdown(f'''<p class="sub-font">COMPARISIONS OF VOLATILITY OF {security} </p>''',unsafe_allow_html=True)
        fig=px.line(df_security,x='DATE',y='VOLATILITY')
        st.plotly_chart(fig,use_container_width=True)

        

    
    
    
    