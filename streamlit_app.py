import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🍲 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🥚 Hard-boiled Free-range egg')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🍍 Build your own fruit Smoothie 🍐🍑')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.pandas(my_fruit_list)
