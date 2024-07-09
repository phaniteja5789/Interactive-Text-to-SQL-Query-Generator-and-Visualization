import streamlit as st
import time
from SessionVariables import InitializationOfSessionVariables,CreationOfCacheSessionVariable
from VannaOpenAIAPI import VannaObjectCreation


def ConnectionToDataBase():

    if not st.session_state.connected:

        # Title of the Streamlit app
        st.title("Connect to the Required Database")

        option = st.selectbox(
            "Connect to the Database",
            ["postgres"],index=0)


        if option == 'postgres':
            st.subheader("Postgres Connection Configuration")
            postgres_user = st.text_input("current_user")
            postgres_password = st.text_input("current password")
            postgres_db = st.text_input("current_database")
            postgres_port = st.text_input("server_port")
            postgres_ip = st.text_input("host")
            
            # Ensure all fields are mandatory
            if postgres_user and postgres_db and postgres_port and postgres_ip and postgres_password:
                connect_button = st.button("Connect To The Database")
                if connect_button:
                    st.session_state.connected = True
                    CreationOfCacheSessionVariable()
                    
                    # Creation of Vanna Object with Llama3 Model
                    vn = VannaObjectCreation(config={'api_key': 'sk-proj-GNHT4noCay7Yp0Gsh3h8T3BlbkFJb40I8ghuyfHKlqdMeGoi', 'model': 'gpt-4-turbo'})
                    returnValue_Connection = vn.ConnectionToPostgres(str(postgres_ip),str(postgres_db),str(postgres_user),str(postgres_password),int(postgres_port))
                    if returnValue_Connection == "Success":

                        st.success("Connected to the Database")
                        time.sleep(0.1)
                        st.session_state.canNavigateToTextToSqlPage = True
                        st.session_state.vn = vn
                        st.switch_page("pages/TextToSQL.py")
                    
                    else:

                        st.error(returnValue_Connection)
                        
            else:
                st.warning("Please fill out all fields")


InitializationOfSessionVariables()
ConnectionToDataBase()