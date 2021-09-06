import streamlit as st
import seaborn as sns
import time

import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

 # Group data together
hist_data = [x1, x2, x3]

group_labels = ['Your biological age', 'Your predicted age', 'Longevity']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])



st.set_page_config(page_title="Age Calc", layout="wide", initial_sidebar_state="expanded", )
sns.set_style("white")

st.title("Aging calculator and therapy recomendation system")
st.markdown("## Your personal anti-aging program")
st.markdown("### To start, choose options to the left!")
st.markdown("____")

factor_1 = st.sidebar.selectbox("Select Factor 1 from the list",
                                           ("None", "Option 1", "Option 2", "Option 3"))

factor_2 = st.sidebar.selectbox("Select Factor 2 from the list",
                                           ("None", "Option 1", "Option 2", "Option 3"))

factor_3 = st.sidebar.number_input("Enter number of cells", 0, value=5, step=1)

factor_4 = st.sidebar.checkbox("Is this factor present?")

factor_5= st.sidebar.radio("Choose one of the options below",
                                     ("Factor 1", "Factor 2", "Factor 3"))

factor_6 = st.sidebar.slider("Select amount of ...", 0.0, 1.5, 0.5, 0.05)

progress_bar = st.sidebar.progress(0)
button = st.sidebar.button("Calculate")

colors = ['lightslategray',] * 5
colors[1] = 'crimson'

fig2 = go.Figure(data=[go.Bar(
    x=['Feature A', 'Feature B', 'Feature C',
       'Feature D', 'Feature E'],
    y=[20, 14, 23, 25, 22],
    marker_color=colors # marker color can be a single color value or an iterable
)])
fig2.update_layout(title_text='Least Used Feature')

import plotly.express as px

df = px.data.gapminder()
df_2007 = df.query("year==2007")

if button:
    for i in range(0, 100):
        progress_bar.progress(i)
        time.sleep(0.05)
    st.plotly_chart(fig)
    st.plotly_chart(fig2)
    
    fig = px.scatter(df_2007,
                     x="gdpPercap", y="lifeExp", size="pop", color="continent",
                     log_x=True, size_max=60,
                     template="plotly_dark", title="System of organs damaged the most")
    st.plotly_chart(fig)