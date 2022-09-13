import streamlit as st
import seaborn as sns
import time

import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
import random

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

senolytics = ['Quercetin', 'Fisetin', 'Dasatinib', '17-DMAG (HSP90 inhibitor)', 'Curcumin analog EF24', 'Epigallocatechin gallate', 'Fenofibrate', 'Rapamycin', 'Azithromycin and Roxithromycin', 'FOXO4 peptide']

 # Group data together
hist_data = [x1, x2, x3]

group_labels = ['Your biological age', 'Your predicted age', 'Longevity']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
fig.update_layout(
    autosize=False,
    width=1100,
    height=600, 
    )
fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))



st.set_page_config(page_title="Age Calc", layout="wide", initial_sidebar_state="expanded", )
sns.set_style("white")

st.title("Aging calculator and therapy recomendation system!!!")
st.markdown("## Your personal anti-aging program")
st.markdown("### To start, choose options to the left!")
st.markdown("____")

factor10_desc = st.sidebar.markdown("**Personal data**")
expand10 = st.sidebar.expander("Click here and fill the requirements")
expand10.number_input("Chronological age (years)", 0, value=30, step=1)
sex = expand10.selectbox("Sex", ["Male", "Female"])
height = expand10.number_input("Height (cm)", 0, value=184, step=1)
weight = expand10.number_input("Body mass (kg)", 0, value=80, step=1)
expand10.success(f"BMI = {round(weight / ((height / 100)**2)), 1}")

factor1_desc = st.sidebar.markdown("**Senescence messaging secretome, SMS**")
expand1 = st.sidebar.expander("Click here and fill the requirements")
expand1.number_input("IL-9 (pg/ml)", 0, value=5, step=1)
expand1.number_input("IL-1α (pg/ml) ", 0, value=5, step=1)
expand1.number_input("IL-2 (pg/ml)", 0, value=5, step=1)
expand1.number_input("IL-6 (fg/ml)", 0, value=274, step=1)
expand1.number_input("MMP-12 (pg/ml) ", 0, value=187, step=1)
expand1.number_input("MMP-2 (pg/ml)", 0, value=93, step=1)
expand1.number_input("FGF-2 (pg/ml)", 0, value=102, step=1)
expand1.number_input("IL-1RA (pg/ml)", 0, value=7, step=1)
expand1.number_input("GM-CSF (pg/ml)", 0, value=10, step=1)


factor2_desc = st.sidebar.markdown("**Brain function test**")
expand2 = st.sidebar.expander("Click here and fill the requirements")
brain_1 = expand2.number_input("Cognitive function (MoCA-test)", 0, value=5, step=1)
brain_2 = expand2.number_input("Depression scale", 0, value=5, step=1)
brain_3 = expand2.number_input("Anxiety scale", 0, value=5, step=1)


factor3_desc = st.sidebar.markdown("**Ophthalmoscopy**")
expand3 = st.sidebar.expander("Click here and fill the requirements")
eyes_1 = expand3.number_input("Lens Opacities Classification System III", 0, value=2, step=1)
eyes_2 = expand3.number_input("Microvascular lesions in retina", 0, value=2, step=1)

factor4_desc = st.sidebar.markdown("**Ultrasonography**")
expand4 = st.sidebar.expander("Click here and fill the requirements")
expand4.number_input("Aortic pulse wave velocity (m/sec)", 0, value=2, step=1)

factor5_desc = st.sidebar.markdown("**Colonoscopy**")
expand5 = st.sidebar.expander("Click here and fill the requirements")
expand5.checkbox("Conventional hyperplastic polyps")
expand5.checkbox("Sessile serrated adenomas")
expand5.checkbox("Traditional serrated adenomas")

factor6_desc = st.sidebar.markdown("**Pulmonary function test**")
expand6 = st.sidebar.expander("Click here and fill the requirements")
expand6.number_input("FEV1 (ml)", 0, value=2, step=1)
expand6.number_input("FEV1/FVC (Tiffeneau-Pinelli index) ", 0, value=2, step=1)
expand6.number_input("MMEF (l/s) ", 0, value=2, step=1)

factor7_desc1 = st.sidebar.markdown("**Bone Densitometry**")
# factor7_desc2 = st.sidebar.markdown("**(Duel-energy X-ray absorptiometry)**")
expand7 = st.sidebar.expander("Click here and fill the requirements")
expand7.number_input("Bone mineral density (BMD) (g/cm2)", 0, value=2, step=1)
expand7.number_input("Bone mineral content (BMC) (kg)", 0, value=2, step=1)

factor8_desc = st.sidebar.markdown("**Kidney function**")
expand8 = st.sidebar.expander("Click here and fill the requirements")
expand8.number_input("Glomerular filtration rate ml/min/1.73m2", 0, value=2, step=1)



factor85_desc = st.sidebar.markdown("**Skin MERZ SCALES**")
expand85 = st.sidebar.expander("Click here and fill the requirements")
expand85.number_input("UPPER FACE", 0, value=2, step=1, max_value=4)
expand85.number_input("MID FACE", 0, value=2, step=1, max_value=4)
expand85.number_input("LOWER FACE", 0, value=2, step=1, max_value=4)
expand85.number_input("NECK", 0, value=2, step=1, max_value=4)
expand85.number_input("PLATYSMA", 0, value=2, step=1, max_value=4)
expand85.number_input("HANDS", 0, value=2, step=1, max_value=4)

factor9_desc = st.sidebar.markdown("**Laboratory test**")
expand9 = st.sidebar.expander("Click here and fill the requirements")
expand9.number_input("HbA1c (µg/mL)", 0, value=2, step=1)
expand9.number_input("Low-density lipoproteins (mmol/l)", 0, value=2, step=1)
expand9.number_input("NT-proBNP (pg/ml)", 0, value=2, step=1)

if sex == 'Male':
    expand9.number_input("PSA (ng/ml)", 0, value=2, step=1)





progress_bar = st.sidebar.progress(0)
button = st.sidebar.button("Calculate")


import plotly.express as px

df = px.data.gapminder()
df_2007 = df.query("year==2007")

if button:
    
    colors = ['lightslategray'] * 6
    damage = [100] * 6
    
    ############################### BRAIN ####################################################
    brain_age = 0
    if brain_1 <= 15:
        brain_age += 1
    if brain_2 >= 33:
        brain_age += 1
    if brain_3 >= 28:
        brain_age += 1
        
        
    if brain_age == 0:
        colors[3] = 'green'
        damage[3] = 100
    elif brain_age == 1:
        colors[3] = 'yellow'
        damage[3] = 80
    elif brain_age == 2:
        colors[3] = 'orange'
        damage[3] = 60
    elif brain_age == 3:
        colors[3] = 'crimson'
        damage[3] = 40
        
    ############################### EYES ####################################################
    eyes_age = 0
    if brain_1 <= 15:
        brain_age += 1
    if brain_2 >= 33:
        brain_age += 1
 
    
    

    fig2 = go.Figure(data=[go.Bar(
        x=['Cardio system', 'Lung system', 'Bone system',
           'Brain system', 'Muscle system', 'Eyes'],
        y=damage,
        marker_color=colors # marker color can be a single color value or an iterable
    )])
    fig2.update_layout(title_text='Healthiness of system of organs')
    fig2.update_layout(
        autosize=False,
        width=1100,
        height=600, 
        )
    fig2.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
    fig2.update_yaxes(range=[0, 100])
    
    
    
    
    for i in range(0, 100):
        progress_bar.progress(i)
        time.sleep(0.05)
    st.plotly_chart(fig)
    st.plotly_chart(fig2)
    
    fig3 = px.scatter(df_2007,
                     x="gdpPercap", y="lifeExp", size="pop", color="continent",
                     log_x=True, size_max=60,
                     template="plotly_dark", title="System of organs damaged the most")
    fig3.update_layout(showlegend=False)
    fig3.update_layout(
    autosize=False,
    width=1100,
    height=600, 
    )
    fig3.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
    st.plotly_chart(fig3)

    #findTherapyButton = st.button("Find optimal senilytics")

    
    
    
    combination = random.sample(senolytics, 2)
    st.success(f'Optimal therapy recomendation: {" and ".join(str(elem) for elem in combination)}')
    
    st.success(f'Brain: {brain_age}')
