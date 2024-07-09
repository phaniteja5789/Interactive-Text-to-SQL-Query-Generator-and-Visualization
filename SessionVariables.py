import streamlit as st

def InitializationOfSessionVariables():

    if "connected" not in st.session_state:
        st.session_state.connected = False

    if "canNavigateToTextToSqlPage" not in st.session_state:
        st.session_state.canNavigateToTextToSqlPage = False

    if "canNavigateToTrainingDataPage" not in st.session_state:
        st.session_state.canNavigateToTrainingDataPage = True

    if "IsInitialTrainingDataHasBeenVectorized" not in st.session_state:
        st.session_state.IsInitialTrainingDataHasBeenVectorized = False


def CreationOfCacheSessionVariable():

    if "cacheDetails" not in st.session_state:
        st.session_state.cacheDetails = {}
        st.session_state.cacheDetails['Questions'] = []
        st.session_state.cacheDetails['SQLResponses'] = []
        st.session_state.cacheDetails['streamed'] = []

def StoringVanna(vn):

    if "vn" not in st.session_state:
        st.session_state.vn = vn

def AppendPromptAndSqlResponseToCache(prompt,response,isstreamed):
    st.session_state.cacheDetails["Questions"].append(prompt)
    st.session_state.cacheDetails["SQLResponses"].append(response)
    st.session_state.cacheDetails["streamed"].append(isstreamed)

def GetCacheDetails():
    return st.session_state.cacheDetails

def GetCachedPairs():
    return len(st.session_state.cacheDetails["Questions"])