import streamlit as st
import pandas as pd
import plotly.express as px
import os
from matplotlib import image


#creating file path for the image and data
FILE_DIR=os.path.dirname(os.path.abspath(__file__))
PARENT_DIR=os.path.join(FILE_DIR,os.pardir)
dir_of_interest=os.path.join(PARENT_DIR,"resources")
IMG_PATH=os.path.join(dir_of_interest,"images","iris.jpg")
DATA_PATH=os.path.join(dir_of_interest,"data","iris.csv")

#reading in image and dataset
img=image.imread(IMG_PATH)
df=pd.read_csv(DATA_PATH)

st.header(":red[IRIS ANALYSIS DASHBOARD]")

#rendering image on streamlit
st.image(img)

st.subheader('Filter dataset by species')

#creating a selectbox to filter dataset by species
species=st.selectbox('Select species:',df['Species'].unique())
filtered_df=df[df["Species"]==species]
st.dataframe(filtered_df)

#creating boxplot based on specie selected
col1,col2=st.columns(2)
fig1=px.box(df[df["Species"]==species],x='PetalLengthCm',title='Statistical analysis of each species Petal length')
col1.plotly_chart(fig1,use_container_width=True)

#correlation plot
fig2 = px.imshow(df.corr(), color_continuous_scale='Plasma', 
labels=dict(x="Features", y="Features", color="Correlation"),title='Correlation between features')
col2.plotly_chart(fig2,use_container_width=True)
