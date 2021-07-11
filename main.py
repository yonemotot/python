import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit入門')

st.write('DataFrame')

df = pd.DataFrame(
  np.random.rand(20,3),
  columns=['a','b','c']
)

st.line_chart(df)
st.write(df)

st.dataframe(df)

st.area_chart(df)
st.bar_chart(df)
# st.markdown("""
# #章
# ##節
# ###項

# '''python
# import streamlit as st
# import numpy as np
# import pandas as pd
# '''
# """)
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
answer = st.button('Say hello')

if answer == True:
     st.write('Why hello there')
else:
     st.write('Goodbye')


agree = st.checkbox('I agree')

if agree == True :
     st.write('Great!')


option = st.selectbox(
    'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)

age = st.slider('How old are you?',  min_value=0, max_value=130, step=1, value=25)
st.write("I'm ", age, 'years old')
values = st.slider(
    'Select a range of values',
   0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)