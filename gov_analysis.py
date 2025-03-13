import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import timedelta

st.set_page_config(page_title="Leads Analysis by Governorates", layout="wide")

def load_data():
    df = pd.read_csv("locations.csv", na_values=["null"])  # Load new dataset
    df['Created On'] = pd.to_datetime(df['Created On'])
    df = df.fillna("")
    return df

df = load_data()

st.sidebar.title("Leads Analysis by Governorates 🌍")
st.sidebar.header("⚙️ Filter")

max_date = df['Created On'].max()
min_date = df['Created On'].min()

default_start_date = max(min_date, max_date - timedelta(days=365))
start_date = st.sidebar.date_input("Start Date", default_start_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

counts = list(df.location.unique())
counts.insert(0,'All locations')
location_selection = st.sidebar.selectbox("Select location", counts )

agents = list(df.Owner.unique())
agents.insert(0,"All agents")
agents_list  = st.sidebar.selectbox("Agent",agents)

df_filtered = df[(df['Created On'] >= pd.Timestamp(start_date)) & (df['Created On'] <= pd.Timestamp(end_date))]

if location_selection !='All locations':
    df_filtered = df_filtered[df_filtered['location']==location_selection]

if agents_list !='All agents':
    df_filtered = df_filtered[df_filtered['Owner']==agents_list]

result_counts = df_filtered['Last Reached Call Result'].value_counts().reset_index()
result_counts.columns = ['Result', 'Count']
print(counts)

st.subheader(f'Governorates results analysis')
st.markdown(f'Location : <b>{location_selection}</b> <br> Agent : <b>{agents_list}</b><br> Total leads = <br>{len(df_filtered)}</b>', unsafe_allow_html=True)

if not result_counts.empty:
    fig1 = px.bar(result_counts, x='Result', y='Count', color='Result', title= "Distribution of Calls Results")
    fig2 = px.pie(result_counts, names='Result', values='Count', title= "Perecentge of each result")

    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)

else:
    st.warning("No data available for the selected date range.")

with st.expander("Display the data 🗂️"):
    st.dataframe(df_filtered)
