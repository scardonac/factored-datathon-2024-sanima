from folium import plugins
import folium

def show_map(data, **kwargs):
    # Initialize map
    map_fig = folium.Map(
        location=[0, 0],
        zoom_start=2,
        tiles='cartodb positron'
    )
    # Add earthquake data with clustering
    marker_cluster = plugins.MarkerCluster().add_to(map_fig)
    # Add all the individual earthquakes to the map
    for _, row in data.iterrows():
        tooltip_text = f"""
        <h5><b>Country:</b> {row['country']}</h5>
        <h5><b>Event:</b> {row['event_code']}</h5>
        """
        #<h5><b>Date:</b> {row['Date']}</h5>
        #color = '#0a9396' if row['Magnitude'] < 4 else '#ee9b00' if row['Magnitude'] < 6 else '#ae2012'
        color = '#0a9396'
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=10,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            weight=0.4,
            tooltip=folium.Tooltip(tooltip_text, sticky=True)
        ).add_to(marker_cluster)
        # Add a search bar
    plugins.Geocoder().add_to(map_fig)
    plugins.MousePosition().add_to(map_fig)
    return map_fig
