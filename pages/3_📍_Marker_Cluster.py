import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("KINMEN Air-Raid Shelter")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = "https://github.com/Peter-eating/hw10.2/raw/refs/heads/main/KINMEN%20Air-Raid%20Shelter%20(1).csv"
        regions = "https://github.com/Peter-eating/hw10.2/raw/refs/heads/main/KINMEN.shp"

        m.add_geojson(regions, layer_name="鄉鎮區界")
        m.add_points_from_xy(
            cities,
            x="Longitude",
            y="Latitude",
            color_column="轄管分局",
            icon_names=["gear", "map"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
