import streamlit as st
st.title("CampusX")

col1, col2 =st.columns(2)

with col1:
    st.image("sample1.jpeg")

with col2:
    st.write(
        """"
        India’s digital public infrastructure (DPI), loosely the India Stack and more, is shaped in a unique partnership between governments (Union and States), regulators, the private sector, selfless volunteers, startups, and academia/think tanks.
        India, through India Stack, became the first country to develop all three foundational DPIs: digital identity (Aadhar), real-time fast payment (UPI) and a platform to safely share personal data without compromising privacy. 
        """
    )

st.header('courses Offered')
st.subheader("data science and machine Learning")
st.subheader("Data Analysis")


st.subheader("power bi")
st.subheader('tablue')

st.sidebar