import streamlit as st 
import datetime
st.set_page_config(page_title='form',layout='wide') 

def AgeCaluculator(birthday):
    try:
        today = datetime.date.today()
        month,day,year = birthday.split('-')
        if  today.month <= int(month):
            if today.day > int(day):
                s = 1 
            else:
                s = 0
        else: 
            s = 0 
        # print('you are ',today.year - int(year) - s , 'years old') 
        st.write('you are {} old'.format(today.year-int(year)-s))

        # print(today.year,year,s)

    except ValueError as e:
        st.write(e)




# st.subheader('Hello welcome to the app')
# st.title('BRUCE WAYNE ENTRIPRISES') 
# st.write('its not who i am underneath but what i do that defines me') 
# st.write('batman vs superman dawn of justice')   

st.markdown("<h1>User Registration</h1>",unsafe_allow_html=True)
with st.form('form2'):
        firstname =  st.text_input('firstname') 
        lastname = st.text_input('lastname')
        submit_button = st.form_submit_button('submit') 
if submit_button:
        one = firstname 
        two = lastname 
        AgeCaluculator(one)
  






# form.text_input('firstname')
# form.form_submit_button("submit")