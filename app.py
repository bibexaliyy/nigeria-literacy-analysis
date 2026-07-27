import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Nigeria Literacy analysis", layout="wide")

df = pd.read_csv('literacy_wide_clean.csv')

st.title("Nigeria Literacy Rate Analysis (1991-2024)")
st.write("This is an analysis showing the literacy rate in Nigeria, a marginal test between men and women, this is aligned towards the direction of gender balance and equity")

latest = df.dropna(subset=['Literacy rate, adult female (% of females ages 15 and above)',
                             'Literacy rate, adult male (% of males ages 15 and above)']).iloc[-1]

col1, col2, col3 = st.columns(3)
col1.metric("Latest Male Literacy", f"{latest['Literacy rate, adult male (% of males ages 15 and above)']:.1f}%")
col2.metric("Latest Female Literacy", f"{latest['Literacy rate, adult female (% of females ages 15 and above)']:.1f}%")
col3.metric("Gender Gap", f"{latest['Literacy rate, adult male (% of males ages 15 and above)'] - latest['Literacy rate, adult female (% of females ages 15 and above)']:.1f} pts")
group = st.sidebar.radio('Choose group:', ['Adult', 'Youth'])
if group == 'Adult':
    female_col = 'Literacy rate, adult female (% of females ages 15 and above)'
    male_col = 'Literacy rate, adult male (% of males ages 15 and above)'
else:
    female_col = 'Literacy rate, youth female (% of females ages 15-24)'
    male_col = 'Literacy rate, youth male (% of males ages 15-24)'

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Year'], y=df[female_col], mode='lines+markers', name='Female'))
fig.add_trace(go.Scatter(x=df['Year'], y=df[male_col], mode='lines+markers', name='Male'))
fig.update_layout(xaxis_title='Year', yaxis_title='Literacy Rate (%)', title=f'{group} Literacy Rate by Gender')
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("Literacy by Wealth Quintile (Young Women 15-24)")
st.write("Data from Nigeria MICS4 (2011) — shows how literacy varies by household wealth, not just gender.")

wealth_data = pd.DataFrame({
    'Quintile': ['Poorest', 'Second', 'Middle', 'Fourth', 'Richest', 'Country Avg'],
    'Literacy Rate (%)': [22, 43, 72, 87, 94, 66]
})

fig2 = go.Figure()
fig2.add_trace(go.Bar(x=wealth_data['Quintile'], y=wealth_data['Literacy Rate (%)']))
fig2.update_layout(xaxis_title='Wealth Quintile', yaxis_title='Literacy Rate (%)')
st.plotly_chart(fig2, use_container_width=True)

st.caption("Note: Gender gap (16 pts) is narrower than the wealth gap (72 pts between poorest and richest) suggesting economic inclusion may matter more than gender alone for literacy outcomes in Nigeria.")
