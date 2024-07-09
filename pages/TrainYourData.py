import streamlit as st
import pandas as pd
from SessionVariables import InitializationOfSessionVariables


def TrainingData():

    if st.session_state.canNavigateToTrainingDataPage:

        tab1,tab2= st.tabs(["Add Training Data","Get the Training Data"])

        
        with tab1:
            
            st.header("Add Initial Database Schema Data to the Vector DB")
            InitializationOfSessionVariables()

            if not st.session_state.IsInitialTrainingDataHasBeenVectorized:

                with st.spinner('Training Data is getting Vectorized'):
        
                    return_value = st.session_state.vn.AddInitialTrainingData()
                    if return_value['content']:
                        st.success("Initial Training Data has been vectorized")
                        st.session_state.IsInitialTrainingDataHasBeenVectorized = True

                    else:
                        st.error(return_value['message'])

            else:

                st.info("Initial Training Data has been already Vectorized")
        
        
        with tab2:
            
            if st.session_state.IsInitialTrainingDataHasBeenVectorized:
            
                st.header("Get the Training Data")

                with st.spinner("Retriving the Training Data... Please Wait..."):

                    return_value = st.session_state.vn.GetTrainingData()

                    if return_value['content']:
                        st.table(return_value['data'])
                    
                    else:

                        st.error(return_value['message'])

            else:

                st.info("Until Training Data has been Vectorized, We cannot get the Training Data")
            
TrainingData()
