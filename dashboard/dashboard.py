import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

df = pd.read_csv("dashboard\main_data.csv")
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://raw.githubusercontent.com/putriraiss/Proyek-Analisis-Data/main/logo.png")
    st.subheader("welcome to Proyek Analisis Data - Bike Sharing\n:fairy::sparkles:")

    st.write(
    """
    Nama: Putri Daliana Salsabilla Rais \n
    Email: putridaliana@gmail.com \n
    ID Dicoding: pptrais \n

    """
    
)
    
st.header(':sparkles::bike: Bike Sharing :bike::sparkles:')

# weather data EDA
st.markdown(
    """
    # Weather Data
    Jumlah Pengguna layanan Bike Sharing berdasarkan Cuaca
    """
)
weather_data = pd.DataFrame({
    'Weathersit': ['Berawan', 'Cerah', 'Salju dan hujan ringan'],
    'Casual': [169776, 446346, 3895],
    'Registered': [827082, 1811606, 33974],
    'cnt': [996858, 2257952, 37869]
})
st.write(weather_data)

# grafik line:
weather_data = {
    'weathersit': ['Berawan', 'Cerah', 'Salju dan hujan ringan'],
    'casual': [169776, 446346, 3895],
    'registered': [827082, 1811606, 33974],
    'cnt': [996858, 2257952, 37869]
}
st.markdown(
    """
    Grafik jumlah pengguna sesuai kondisi cuaca
    """
)
weather_sum = pd.DataFrame(weather_data)
weather_sum_melted = pd.melt(weather_sum, id_vars='weathersit', var_name='user_type', value_name='count')

fig = px.line(weather_sum_melted, x='weathersit', y='count', color='user_type', markers=True,
              labels={'count': 'Jumlah Pengguna', 'weathersit': 'Kondisi Cuaca'},
              title='Tren Penggunaan Layanan Bike Sharing Berdasarkan Kondisi Cuaca')
fig.update_xaxes(type='category', tickmode='array', tickvals=weather_sum['weathersit'],
                 ticktext=['Berawan', 'Cerah', 'Salju dan Hujan Ringan'])
st.plotly_chart(fig)

# Hasil analisis
st.markdown(
    """
    ## Presentase Penggunaan Layanan Bike Sharing Berdasarkan Kondisi Cuaca
    """
)
weather_sum = df.groupby('weathersit').sum().reset_index()
weather_sum.index = ['Berawan', 'Cerah', 'Salju dan hujan ringan']

total_rentals = weather_sum['cnt'].sum()
proportions = weather_sum['cnt'] / total_rentals * 100

colors = ['darkblue', 'skyblue', 'lightblue']

fig = px.pie(weather_sum, values='cnt', names='weathersit', hole=0.3, color_discrete_sequence=colors)
fig.update_layout(title='Persentase dari penggunaan Bike Sharing Sesuai Cuaca')

st.plotly_chart(fig)

st.markdown(
    """ 
    **Bagaimana dampak dari kondisi cuaca terhadap penggunaan layanan bike sharing?**\n
    Dari diagram di atas dapat disimpulkan bahwa cuaca memang berdampak terhadap penggunaan 
    layanan bike sharing dikarenakan jika melihat pada diagram di atas dapat disimpulkan 
    banyak pengguna yang lebih suka menggunakan layanan tersebut ketika cuaca sedang cerah 
    dengan presentase pengguna sebanyak 68.6%, begitupula sebaliknya banyak yang tidak menggunakan 
    layanan bike-sharing ketika cuaca sedang salju atau hujan ringan dengan presentase hanya sebesar 1.2%.

    """
)

# SEASON
st.markdown(
    """
    # Season Data
    Jumlah Pengguna layanan Bike Sharing berdasarkan 4 Musim
    """
)

seasonal_info = pd.DataFrame({
    'Season': ['Fall', 'Spring', 'Summer', 'Winter'],
    'Casual': [226091, 60622, 203522, 129782],
    'Registered': [835038, 410726, 715067, 711831],
    'cnt': [1061129, 471348, 918589, 841613]
})
st.write(seasonal_info)

# grafik bar
st.markdown(
    """
    Grafik bar jumlah pengguna layanan bike sharing berdasarkan musim
    """
)
total_users_per_season_sorted = pd.DataFrame({
    'season': ['Fall', 'Spring', 'Summer', 'Winter'],
    'casual': [1562, 985, 801, 1349],
    'registered': [1454, 654, 670, 1229],
    'cnt': [3016, 1639, 1471, 2578]
})
st.bar_chart(total_users_per_season_sorted.set_index('season'))

# Hasil analisis
st.markdown(
    """
    ## Presentase Penggunaan Layanan Bike Sharing Berdasarkan Musim (4 Musim)
    """
)
total_users_per_season = df.groupby('season')['cnt'].sum().reset_index()
total_rentals = total_users_per_season['cnt'].sum()
proportions = total_users_per_season['cnt'] / total_rentals

colors = ['#1f78d3', '#4575b4', '#91bfdb', '#a6bddb']

fig = px.pie(total_users_per_season, values='cnt', names='season', hole=0.3, color_discrete_sequence=colors)
fig.update_layout(title='Persentase Penggunaan Bike Sharing per Musim')

st.plotly_chart(fig)

st.markdown(
    """ 
    **Tingkat peminjaman sepeda terendah terjadi di musim apa??**\n
    Dari diagram di atas  dapat disimpulkan bahwa peminjaman sepeda 
    terendah terjadi pada musim "spring" atau "semi", hal tersebut dapat 
    dibuktikan dengan jumlah presentase diagram di atas di mana spring 
    hanya sebesar 14.3%. Sedangkan untuk pengguna terbanyak menggunakan 
    layanan bike-sharing ialah pada musim "Fal" atau "gugur" dengan presentase sebesar 32.2%.
    """
)

st.caption('Copyright (c) 2024')
