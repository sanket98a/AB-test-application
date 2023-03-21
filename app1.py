import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import abtest as ab
st.title("A/B TESTING")
st.write('Use this free bayesian A/B testing calculator to find out if your test results are statistically significant. For each variation you tested, input the total sample size, and the number of conversions.')

with st.sidebar.form("my_form"):
   st.write("Submit The Details")
   prior_beta=st.select_slider('Prior Beta',range(1,1000))
   prior_alpha=st.select_slider('Prior Alpha',range(1,1000))
   Control = st.selectbox('Control',
     range(1,10000))
   Treatment = st.selectbox('Treatment',
     range(1,10000))
   Control_total = st.selectbox('Total Control',
     range(1,10000))
   Treatment_total = st.selectbox('Total Treatment',
     range(1,10000))
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")


# Now add a submit button to the form:
# st.sidebar.button("Submit",ab.BayesianApproach(Control,Treatment,Control_total,Treatment_total))

probability,ans,lift,treatment_samples,control_samples,color=ab.BayesianApproach(Control,Treatment,Control_total,Treatment_total)
# st.image()
try:
    st.write(f"Result :: {ans}",unsafe_allow_html=True)
    # chart_data=[0.80,0.20]
    plt.bar(x=['Treatment','Control'],height=[probability,1-probability],color=color)
    plt.hlines(0.95,-1,2)
    plt.text(x=-1,y=0.96,s='Terminate>=0.95')
    plt.ylim(0,1)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    st.subheader("Posterior simulation of difference")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.kdeplot(treatment_samples,label='Treatment')
    sns.kdeplot(control_samples,label='Control')
    plt.legend()
    st.pyplot() 
except:
    st.write('This app walkthroughs on creating your first data app with streamlit')

