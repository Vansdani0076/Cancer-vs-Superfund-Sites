
import streamlit as st
import plotly.io as pio
import plotly.graph_objects as go

st.title("Cancer Rates and Superfund Site Proximity Dashboard")

st.header("📊 Cancer Rates by County")
bar_chart = pio.from_json(open("dashboard_bar_chart.json").read())
st.plotly_chart(bar_chart)

st.header("🔄 Correlation: Superfund Sites vs Cancer Rate")
scatter_plot = pio.from_json(open("dashboard_scatter_plot.json").read())
st.plotly_chart(scatter_plot)

st.header("🗺️ Geographic Distribution Map")
st.markdown("Download and view the interactive map using Plotly viewer:")
with open("dashboard_map.json", "r") as f:
    st.download_button("Download Map JSON", f.read(), file_name="dashboard_map.json")
