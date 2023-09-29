import streamlit as st
st.title("CampusX")

col1, col2 =st.columns(2)

with col1:
<<<<<<< HEAD
    st.image("sample3.jpg")
=======
    st.title("Hi")
>>>>>>> sidebar

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

st.sidebar.title("Menu")
st.sidebar.markdown("""
                    -Home

                    -About
                    
                    -contact

                    -Career 

                    -Login
""")

st.sidebar.selectbox("select one",["teacher", "student"])
st.sidebar.button("select")

st.sidebar.selectbox("Login as",["teacher", "student"])
st.sidebar.button("login page")

st.sidebar.selectbox("select course",["DSPM", "DSA"])
st.sidebar.button("select")
