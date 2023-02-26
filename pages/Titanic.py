import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os  

#using os to get file path of image and dataset
FILE_DR=os.path.dirname(os.path.abspath(__file__))
PARENT_DIR=os.path.join(FILE_DR,os.path.pardir)
dir_of_interest=os.path.join(PARENT_DIR,"resources")
IMAGE_PATH=os.path.join(dir_of_interest,"images","titanic.jpg")
DATA_PATH=os.path.join(dir_of_interest,"data","titanic.csv")

#reading in image and data
img=image.imread(IMAGE_PATH)
df=pd.read_csv(DATA_PATH)

st.header(':red[TITANIC ANALYSIS DASHBOARD]')
#rendering image to streamlit
st.image(img)

st.subheader('Filter the dataset by gender')

#creating a selectbox to filter dataset by gender
sex=st.selectbox("Select gender",df['sex'].unique())
filtered_df=df[df['sex']==sex]
st.dataframe(filtered_df)

#creating histogram to show surviving passengers per city
col1,col2=st.columns(2)
fig1=px.histogram(df[df['alive']=='yes'],x='embark_town',title='Count of surviving passengers per city')
col1.plotly_chart(fig1,use_container_width=True)

#creating a pie chart to show passengers per class
import plotly.graph_objs as go
#aggregate dataframe to get count of people in each clas
agg_df=df.groupby('class')['class'].count()
#create piechart trace
trace = go.Pie(labels=agg_df.index, values=agg_df.values)
#create a layout
layout = go.Layout(title='Count of passenegers per class')
#create a figure object
fig = go.Figure(data=[trace], layout=layout)
col2.plotly_chart(fig,use_container_width=True)
