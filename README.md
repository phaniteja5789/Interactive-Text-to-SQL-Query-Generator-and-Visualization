# Text2SQL

Problem Statement - Given the Input Text Prompt, we need to generate the relevant SQL responsible for that and along with that we need to Visualization Plot based on the result and along with that we need to generate the Follow-Up prompts based on the prompt we asked initially

Tech Stack used - Streamlit, OPENAI API, VANNA, Postgres

Execution Phases

  The Project has been implemented and executed in 4 Phases.

  Phase - 1 ==> Connection to the Database
            ==> In the 1st Phase, created a UI Page where the actual execution starts
            ==> Connection to the Database. We can connect to any database as per our requirement.
            ==> I have taken Postgres database. Once the database has been choosen, based on the database choosen, the connection string parameters will be updated
            ==> For the Postgres database, the connection string parameters are Host,UserName,Password,Port,Database
            ==> I am providing these options needs to be entered by the user.
            ==> Once these details has been entered by the user, these details will be validated and based on the validation, it will proceed further.
            ==> Once it gets connected to the database, the status will be shown to the user as below Image.
            <img width="1103" alt="image" src="https://github.com/phaniteja5789/Text2SQL/assets/36558484/72171e10-ca5b-4a06-b86f-9c8eb109c2b8">
            ==> After successful connect to the Database, it will navigate to the TextToSQL Page, where user can enter the chat information

  Phase - 2 ==> Training with Database data
            ==> Here I am using the RAG in order to train the Tabular data and schema information present in the table.
            ==> Every information will be Vectorized and the vectors will be stored in the ChromaDB
            ==> During the vectorization phase, the user will be get to know, that the data is getting vectorized as per below image.
            <img width="1102" alt="image" src="https://github.com/phaniteja5789/Text2SQL/assets/36558484/868919c1-f088-4470-9a90-c39a4715e89b">
            ==> After the Vectorization phase is completed, the user will get to know, the training has been completed by the status image as per below image.
            <img width="1100" alt="image" src="https://github.com/phaniteja5789/Text2SQL/assets/36558484/5084eb7d-8bb6-45b9-b786-d86f02788b2f">
            ==> Once the Vectorization phase is done, the user can see the training data information in the next tab of the TrainYourData page as per below image.
            <img width="1102" alt="image" src="https://github.com/phaniteja5789/Text2SQL/assets/36558484/bd7b8244-ab6e-4ea5-a110-e7c8662ca565">
  
  Phase - 3 ==> Chat with your Data
            ==> Here, user can give the Input Prompt, based on the Input Prompt, the SQL query will be generated and also a CSV file will be provided as an option to download to view the result
            ==> Along with that the Plotly Chart also will be generated and along with that the Followup Prompts also will be generated where user can ask these prompts next time.
            ==> See the below Images for output
            <img width="1101" alt="image" src="https://github.com/phaniteja5789/Text2SQL/assets/36558484/ac9ff77e-f556-4da3-b151-e209611a1bec">
            <img width="1102" alt="image" src="https://github.com/phaniteja5789/Text2SQL/assets/36558484/8563cf2a-fad4-4c26-8961-ae37e6b1cfa7">
            <img width="1099" alt="image" src="https://github.com/phaniteja5789/Text2SQL/assets/36558484/e77d0f3f-9d36-46f8-8700-6eb28ff73beb">
            <img width="739" alt="image" src="https://github.com/phaniteja5789/Text2SQL/assets/36558484/5034f0fb-6b82-435f-ae0c-c31b3aa54769">

  Phase - 4 ==> Cache Details
            ==> Whatever the Input Prompts user has entered and whatever the SQL Responses generated are stored in the QuestionsANDResponses Page. 
            ==> Attached the below image for the cache details
            <img width="1103" alt="image" src="https://github.com/phaniteja5789/Text2SQL/assets/36558484/bd464d36-2681-444e-8032-ced88d972aed">

The development phase can be extended with use cases like generating the summary of the schema etc.

The Output can be seen in the TextToSQL.mp4 file which is part of this repository.



            


            
