import Pandas as pd
import streamlit as st
tabla={"adat1":[1,2,3,4,5],
       "adat2":[6,7,8,9,10]}
kiiras=st.data_editor(pd.dataframe(tabla))
st.write(kiiras)
