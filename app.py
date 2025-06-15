import streamlit as st

st.title(" MDCAT CALCULATOR ")
marks=st.number_input("enter marks out of 180", min_value=0.0 , max_value=180.0 )
if marks>= 170:
      st.success("kmc,amc,kgmc!")
elif marks>= 165:
      st.info("bkmc,smc,nmc!")
elif marks>= 155:
      st.warning("gkmc,gmc,bmc,kims!")
else:
      st.error("not in mbbs")

