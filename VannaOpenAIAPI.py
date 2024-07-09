from vanna.openai import OpenAI_Chat
from vanna.chromadb.chromadb_vector import ChromaDB_VectorStore
import streamlit as st

class VannaObjectCreation(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)


    def ConnectionToPostgres(self,host,dbname,user,password,port):
        try:
            self.connect_to_postgres(host=host,dbname=dbname,user=user,password=password,port=port)
            return "Success"
        except Exception as e:
            return e

    def AddInitialTrainingData(self):
        try:
            df_information_schema = self.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")
            plan = self.get_training_plan_generic(df_information_schema)
            st.session_state.vn.train(plan = plan)
            
            return dict(
                {
                    "content" : True
                }
            )
        except Exception as e:
            return dict(
                {
                    "content" : False,
                    "message" : e
                }
            )

    def GetTrainingData(self):
        try:

            df = self.get_training_data()

            return dict(
            {
                "data": df,
                "content" : True
            })
        
        except Exception as e:
            return dict(
                {
                    "content" : False,
                    "message" : e
                })

    def GenerateQuestions(self):
        try:

            questions_list = self.generate_questions()

            return dict(
                {
                    "content" : True,
                    "questions_list" : questions_list
                }
            )
        
        except Exception as e:

            return dict(
                {
                    "content" : False,
                    "message" : e
                }
            )

    def GenerateSQL(self,question):

        try:

            sql = self.generate_sql(question = question,allow_llm_to_see_data=True)

            return dict(
                {
                    'content' : True,
                    'return_sql' : sql
                }
            )
        
        except Exception as e:

            return dict(
                {
                    'content': False,
                    "message":e
                }
            )

    def RunSQL(self,sql):

        try:

            df = st.session_state.vn.run_sql(sql = sql)
            return dict(
                {
                    'content' : True,
                    'return_df' : df
                }
            )
        except Exception as e:

            return dict(
                {
                    'content' : False,
                    'message' : e
                }
            )
        
    def GeneratePlot(self,df,question,sql):
        try:
            #code = self.generate_plotly_code(question=question, sql=sql, df_metadata=f"Running df.dtypes gives:\n {df.dtypes}")
            code = self.generate_plotly_code(question=question, sql=sql, df=df)
            fig = self.get_plotly_figure(plotly_code=code, df=df, dark_mode=True)
            st.plotly_chart(fig,use_container_width=True)
            
            return dict(
                {
                    'content' : True,
                    'message' : "success"
                }
            )
        except Exception as e:

            return dict(
                {
                    'content' : False,
                    'message':e
                }
            )

    def GenerateFollowUpQuestions(self,df,question,sql):
        try:
            
            followup_questions = self.generate_followup_questions(sql=sql,question=question,df= df)

            return dict(
                {
                    'content':True,
                    'return_follow_up_questions' : followup_questions
                }
            )
        except Exception as e:

            return dict(
                {
                    'content' : False,
                    "message":e
                }
            )