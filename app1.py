
import streamlit as st

st.title('Graded Assignment 8')
st.subheader('Finding whether the given number is odd or even.')
placeholder_number = st.empty()

n = placeholder_number.number_input('Enter The Number',step=1)

if n>=0 and int(n)%2 != 0:
	st.write("This is Odd number !! ")  
elif n>=0 and int(n)%2 == 0:
    st.write("This is Even number !! ")
        
else:
    st.write(" Please Enter a valid Integer.")    