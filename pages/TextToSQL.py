import streamlit as st
import time
import pandas as pd
import numpy as np
from SessionVariables import InitializationOfSessionVariables,AppendPromptAndSqlResponseToCache,GetCacheDetails,GetCachedPairs

# Generates the Follow Up Questions based on the Query
def displayFollowUpQuestions(df,question,sql):
    return_followup = st.session_state.vn.GenerateFollowUpQuestions(df,question,sql)
    if return_followup['content']:
        return return_followup['return_follow_up_questions']
    else:
        st.error(return_followup['message'])
        return None

# Generates the Downloadable Results File 
def displayDownloadableResultsFile(result):
    st.download_button(
    label="Download data as CSV",
    file_name="result.csv",
    data = result.to_csv().encode("utf-8"),
    mime="text/csv",
    )
    return 0

def createGeneratorObjectForSQLResponse(sqlResponse):
    for word in sqlResponse.split(" "):
        yield word + " "
        time.sleep(0.02)
    
def generate_sql(prompt):

    return_sql = st.session_state.vn.GenerateSQL(prompt)
    if return_sql['content']:
        return return_sql["return_sql"]
    else:
        st.error(return_sql["message"])
        return None

def run_sql(sql):
    return_df = st.session_state.vn.RunSQL(sql)
    if return_df["content"]:
        return return_df["return_df"]
    else:
        st.error(return_df["message"])
        return None

def DisplayPlot(question,sql,results):
    return_fig = st.session_state.vn.GeneratePlot(results,question,sql)
    if return_fig['content']:
        return return_fig['message']
    else:
        st.error(return_fig['message'])
        return None

def displayEarlierMessages():

    cache_details = GetCacheDetails()
    total_pairs = GetCachedPairs()
    for i in range(0,total_pairs):
        st.chat_message("user").write(cache_details["Questions"][i])
        if not cache_details["streamed"][i]:
            st.chat_message("assistant").write_stream(createGeneratorObjectForSQLResponse(cache_details["SQLResponses"][i]))
            cache_details["streamed"][i] = True
        else:
            st.chat_message("assistant").write(cache_details["SQLResponses"][i])
        
def ChatInput():
    if st.session_state.canNavigateToTextToSqlPage:
        
        if prompt := st.chat_input("Enter your Input Prompt"):
            
            return_val = generate_sql(prompt)
            if return_val is None:
                return
            
            AppendPromptAndSqlResponseToCache(prompt,return_val,False)

            displayEarlierMessages()

            return_df = run_sql(return_val)
            if return_df is None:
                return
            
            displayDownloadableResultsFile(return_df)

            return_fig = DisplayPlot(prompt,return_val,return_df)
            
            if return_fig is None:
                return
            
            followup_questions = displayFollowUpQuestions(return_df,prompt,return_val)

            if followup_questions is None:
                return
            
            for question in followup_questions:

                st.text(question)

InitializationOfSessionVariables()
ChatInput()