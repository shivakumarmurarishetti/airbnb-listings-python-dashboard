import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("cleaned_listings.csv")

# Set up the dashboard configuration
st.set_page_config(page_title="Airbnb Dashboard", layout="wide")
st.markdown("<h1 style='text-align: center;'>🏘️ Airbnb Insights Dashboard</h1>", unsafe_allow_html=True)

# Sidebar filters
st.sidebar.header("🎛️ Explore Listings")
neighbourhoods = sorted(df['neighbourhood_group'].unique())
room_types = sorted(df['room_type'].unique())

selected_neighbourhoods = st.sidebar.multiselect("📍 Neighbourhood Group(s)", neighbourhoods, default=neighbourhoods)
selected_room_types = st.sidebar.multiselect("🏠 Room Type(s)", room_types, default=room_types)
min_price, max_price = st.sidebar.slider("💵 Price Range ($)", 0, 1500, (50, 500))

# Search box to filter across name, neighbourhood, or room type
search_term = st.text_input("🔍 Search Listings (by Name, Neighbourhood or Room Type)")
if search_term:
    search_term = search_term.lower()
    search_df = df[
        df['name'].fillna("").astype(str).str.lower().str.contains(search_term) |
        df['neighbourhood_group'].fillna("").astype(str).str.lower().str.contains(search_term) |
        df['room_type'].fillna("").astype(str).str.lower().str.contains(search_term)
    ]
else:
    search_df = df.copy()

# Apply selected filters to the searched data
filtered_df = search_df[
    (search_df['neighbourhood_group'].isin(selected_neighbourhoods)) &
    (search_df['room_type'].isin(selected_room_types)) &
    (search_df['price'].between(min_price, max_price))
]

# Display summary statistics
st.subheader("📊 Summary Overview")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Listings", f"{filtered_df.shape[0]:,}")

with col2:
    avg_price = filtered_df['price'].mean()
    st.metric("Avg Price", f"${avg_price:.2f}" if not pd.isna(avg_price) else "N/A")

with col3:
    most_common_room = filtered_df['room_type'].mode()[0] if not filtered_df.empty else "N/A"
    st.metric("Most Frequent Room Type", most_common_room)

# Interactive chart options using buttons
st.subheader("🎛️ Interactive Chart Viewer")

if 'chart_choice' not in st.session_state:
    st.session_state.chart_choice = "room"

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📊 Room Type Count"):
        st.session_state.chart_choice = "room"

with col2:
    if st.button("📈 Price vs Reviews"):
        st.session_state.chart_choice = "price_review"

with col3:
    if st.button("🗺️ Map of Listings"):
        st.session_state.chart_choice = "map"

with col4:
    if st.button("📉 Price Distribution"):
        st.session_state.chart_choice = "distribution"

chart_choice = st.session_state.chart_choice

# Display the selected chart
if chart_choice == "room":
    room_counts = filtered_df['room_type'].value_counts().reset_index()
    room_counts.columns = ['room_type', 'count']
    fig = px.bar(room_counts, x='room_type', y='count', text='count', color='room_type',
                 title="Room Type Distribution")
    fig.update_traces(textposition='outside')
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    st.write("💡 Most listings are either private rooms or entire homes.")

elif chart_choice == "price_review":
    fig = px.scatter(filtered_df, x='price', y='number_of_reviews', color='room_type',
                     hover_data=['name'], title="Price vs Number of Reviews")
    st.plotly_chart(fig, use_container_width=True)
    st.write("💡 Listings with a high number of reviews are typically priced below $300.")

elif chart_choice == "map":
    min_reviews = st.slider("Minimum Reviews for Map", 0, 200, 10)
    map_df = filtered_df[filtered_df['number_of_reviews'] >= min_reviews]
    fig = px.scatter_mapbox(map_df, lat="latitude", lon="longitude", color="room_type",
                            size="number_of_reviews", hover_name="name", mapbox_style="carto-positron",
                            zoom=10, title="Listings Map (Filtered by Reviews)")
    st.plotly_chart(fig, use_container_width=True)
    st.write("💡 Higher review listings are concentrated in central areas like Manhattan and Brooklyn.")

elif chart_choice == "distribution":
    fig = px.histogram(filtered_df, x='price', nbins=50, title="Price Distribution")
    st.plotly_chart(fig, use_container_width=True)
    st.write("💡 Most listings fall under $300, with fewer high-end options.")

# Display top 5 most expensive listings
st.subheader("💰 Top 5 Most Expensive Listings")
if not filtered_df.empty:
    top_expensive = filtered_df.sort_values(by='price', ascending=False).head(5)
    st.dataframe(top_expensive[['name', 'neighbourhood_group', 'room_type', 'price']])
else:
    st.info("No listings available to display.")

# Show the filtered dataset
st.subheader("📄 Filtered Listings Table")
if not filtered_df.empty:
    st.dataframe(filtered_df[['name', 'neighbourhood_group', 'room_type', 'price', 'number_of_reviews']],
                 use_container_width=True)
    st.download_button("📥 Download as CSV", data=filtered_df.to_csv(index=False),
                       file_name="filtered_listings.csv", mime="text/csv")
else:
    st.warning("No listings match the selected filters or search.")

# Option to show descriptive stats
if st.checkbox("📊 Show Descriptive Statistics"):
    st.write(filtered_df.describe())

# Footer
st.markdown("---")
st.markdown("Shiva Kumar Murarishetti | Data Source: Airbnb Open Data", unsafe_allow_html=True)
