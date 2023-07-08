import streamlit as st
st.set_page_config(page_title="BUNK CALCULATOR ",page_icon="tada",layout="wide")

st.header(":red[BUNK] :blue[CALCULATOR]")
def calc(credit,abs):
    if (credit==1):
        if(abs<3):
           bunk=2-abs
        else:
            bunk=-1

    elif (credit==2):
        if(abs<6):
            bunk=5-abs
        else:
            bunk=-1
    elif (credit==3):
        if(abs<9):
            bunk=8-abs
        else:
            bunk=-1 
    elif (credit==4):
        if(abs<12):
            bunk=11-abs
        else:
            bunk=-1
    else:
       bunk=0
    return bunk

col1,col2,col3=st.columns(3)

with col1:
    credit=st.selectbox(":blue[Credit of the Course]",options=[4,3,2,1])
    abs = st.slider(':blue[How Many Absent so far]', min_value=1, max_value=12,step=1)

bunk=calc(credit,abs)


if st.button("Submit"):
    if(bunk >=0):
       st.subheader(":green[REMAINING BUNK:]");st.subheader(bunk)
    else:
         st.subheader("ATTENDANCE IS < 80 % ")
         st.markdown(":red[Attend UpComing Classes]  :shushing_face:")
         
