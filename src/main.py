'''
 # @ Author: Adam Zhang
 # @ Create Time: 2023-08-15 20:51:09
 # @ Modified by: Adam Zhang
 # @ Modified time: 2023-08-16 13:43:12
 # @ Description: simple app to learn langchain from tutorial
'''

import streamlit as st
import langchain_helper



st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Select a cuisine", 
                     ["Chinese", "Indian", "Italian", "Mexican", "Thai"])



if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response["restaurant_name"].strip())
    
    # get a list of menu items
    menu_items = response["menu_items"].strip().split(",")
    
    st.write("Menu Items")
    for item in menu_items:
        st.write("-",item)
