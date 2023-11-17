import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os



df=pd.read_csv(r'C:\Users\hendr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\submission\dashboard\main.csv')

musim = {1: 'Semi', 2: 'Panas', 3: 'Gugur', 4: 'Dingin'}

st.title('Analisis Data Rental Sepeda')

st.sidebar.header('Pilih Musim')

selected_musim = st.sidebar.selectbox('Pilih Musim untuk dianalisis', sorted(musim.values()))

musim_data = {v: k for k, v in musim.items()}[selected_musim]

data = df[df['season'] == musim_data]

st.header(f'Untuk Musim {selected_musim}')

fig= plt.figure(figsize=(8, 6))
sns.violinplot(x='workingday', y='cnt', data=data)
plt.xlabel('Hari Kerja atau Hari Libur')
xlabels = ['Hari Libur','Hari Kerja']
x = np.arange(len(xlabels))
plt.xticks(x, labels=xlabels)
plt.ylabel('Count of Rentals')
st.pyplot(fig)