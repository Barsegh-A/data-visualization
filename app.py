import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def get_data():
    df = pd.read_excel('Data Model - Pizza Sales.xlsx')

    return df


def main():

    st.set_page_config(layout='centered')
    
    df = get_data()

    st.title('Pizza Sales Visualization')
    
    st.header('**Sample from data**')
    st.dataframe(df.head(10))
    
    st.header('**Pizza Size Distribution**')
    size_counts = df['pizza_size'].value_counts()
    st.bar_chart(size_counts)

    st.header('**Pizza Category Distribution**')
    category_counts = df['pizza_category'].value_counts()
    st.bar_chart(category_counts)

    st.header('**Pizzas by Given Category**')
    pizza_category = st.selectbox('Select Pizza Category', df['pizza_category'].unique())
    st.write(df[df['pizza_category']==pizza_category]['pizza_name'].unique())

    st.header('**Pizza Ingredients**')
    pizza_name = st.selectbox('Select Pizza', df['pizza_name'].unique())
    st.write(' ,'.join(df[df['pizza_name']==pizza_name]['pizza_ingredients'].unique()))

    
    st.header('**Pizza Orders**')
    time = st.selectbox('Select time variable', ['Month', 'Day of Week', 'Hour'])
    if time == 'Month':
        df['month'] = df['order_date'].dt.month_name()
        orders_by_month = df['month'].value_counts()
        st.bar_chart(orders_by_month)
    elif time == 'Day of Week':
        df['day_of_week'] = df['order_date'].dt.day_name()
        orders_by_day = df['day_of_week'].value_counts()
        st.bar_chart(orders_by_day)
    else:
        df['hour'] = pd.to_datetime(df['order_time'], format='%H:%M:%S').dt.hour
        orders_by_hour = df['hour'].value_counts().sort_index()
        st.line_chart(orders_by_hour)



if __name__ == '__main__':
    main()