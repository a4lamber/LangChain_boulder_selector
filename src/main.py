'''
 # @ Author: Adam Zhang
 # @ Create Time: 2023-08-17 11:12:48
 # @ Modified by: Adam Zhang
 # @ Modified time: 2023-08-17 11:12:58
 # @ Description: PoC for boulder router selector app
'''

import streamlit as st
from langchain_boulder import LangchainBoulder


def main():
    st.title("Boulder Router Selector App")

    # Add a text input widget for location entry
    location = st.text_input("Enter your location:")


    # Add a button to save the location
    location_button_state = st.button("Save Location")

    if location_button_state:
        st.success(f"Location saved as {location}")  
        
        
    # Call LLM to get a list of parks
    parks = LangchainBoulder.get_boulder_parks(location)

    selected_park = st.selectbox("Select a park", parks)

    # Select climbing difficulty
    selected_difficulties = st.selectbox("Select a difficulty", 
                                            ["V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7"])

    climb_button = st.button("Go Climb!")

    if climb_button:
        # 创造一个markdown table
        table = LangchainBoulder.get_boulder_tables(selected_park, selected_difficulties)
        st.markdown(table)
        

if __name__ == "__main__":
    main()
