import streamlit as st
from streamlit_folium import st_folium, folium_static

from services import database_service
from components import maps
from utils import data_processing


st.title("News Analysis", )

col1, col2 = st.columns([2, 4], vertical_alignment="center")


with col1:
    st.selectbox(
        "Fecha", ["top", "center", "bottom"], index=1
    )
    st.selectbox(
        "Tema", ["top", "center", "bottom"], index=2
    )
    st.selectbox(
        "País", ["top", "center", "bottom"], index=2
    )

with col2:
    st.header("Global Summary")
    st.markdown(
        """
        Lorem ipsum dolor sit amet consectetur adipiscing elit mollis 
        libero et integer viverra, pretium sociis consequat vestibulum 
        nostra felis fermentum nulla lectus eleifend hac dictumst fames, 
        rutrum ullamcorper convallis blandit natoque non volutpat congue 
        proin gravida venenatis.
    """
    )

# Load the dataset
@st.cache_data
def load_data():
    data = database_service.get_data()
    return data

data = load_data()
processed_data = data_processing.process_data(data)

# Show the map
# st_data = st_folium(maps.show_map(processed_data['news']), width=500, height=300)
# print(st_data)
folium_static(maps.show_map(processed_data['news']))
st.dataframe(processed_data['news']) 
