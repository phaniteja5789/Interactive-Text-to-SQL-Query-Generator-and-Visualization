import streamlit as st
import pandas as pd


questions_list = st.session_state.cacheDetails["Questions"]
sql_responses_list = st.session_state.cacheDetails["SQLResponses"]

table_data = pd.DataFrame(
    {
        "Questions_Asked" : questions_list,
        "Answers_Responded" : sql_responses_list
    }
)

st.table(table_data)