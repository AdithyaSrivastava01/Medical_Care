# VistaCare: AI-Powered Medical Query Assistant (RAG-Based Web App)

This project leverages a Retrieval-Augmented Generation (RAG)-based web application that answers medical-related queries accurately. The system ingests knowledge from a medical book titled *The GALE ENCYCLOPEDIA of MEDICINE SECOND EDITION*, enabling it to generate informed and reliable responses. The project implements an LLM-based retrieval and contextual augmentation to enhance accuracy. The application ensures efficient query resolution and improves medical information accessibility through a user-friendly web interface. 

---

## Features  

- **Medical Query Assistant**: Implements a RAG-based approach to answer the medical queries provided by the user
- **Gen-AI interface**: Incorporate cloud-based vector database Pinecone coupled with HuggingFace sentence transformers for Embedding and OpenAI API for LLM integration into the application. 
- **User-Friendly Web Application**: Developed using Flask, HTML, and CSS for real-time predictions.  
- **Cloud Deployment**: Hosted on AWS EC2 and AWS ECR for robust and scalable access.  
- **Automation Integration**: Deployed via GitHub Actions for seamless CI/CD.  

---

## Tech Stack  

- **Programming Languages**: Python, HTML, CSS, JQuery
- **Web Framework**: Flask
- **Gen-AI Tools**: Pinecone(vector database), LangChain, HuggingFace, OpenAI API(LLM)
- **Deployment/ Cloud Tools**: Docker, AWS EC2, AWS ECR 
- **CI/CD Tools**: GitHub Actions  

---

## File Structure  

```plaintext
performance_index_project/
│
├── notebook/
│   ├── data/
│   │   └── stud.csv                 # Public Dataset
│   ├── EDA STUDENT.ipynb            # EDA and visualization of the data
│   └── MODELTRAINING.ipynb          # Model Training Notebook
│
├── artifacts/                 
│   ├── model.pkl                    # Pretrained model for prediction
│   ├── test.csv                     # Dataset used for testing
│   ├── train.csv                    # Dataset used for training
│   └── processor.pkl                # Preprocessor used during prediction stage
│
├── src/                             # Main scripts
│   ├── components/         
│   │    ├── data_ingestion.py       # Data Ingestion file
│   │    ├── data_transformation.py  # Data transformation file
│   │    └── model_trainer.py        # Model Training file
│   │
│   ├── pipeline/       
│   │    └── predict_pipeline.py     # Prediction Pipeline file
│   │
│   ├── exception.py                 # Exception Handling file
│   ├── logger.py                    # Logger file to log activities
│   └── utils.py                     # Utility script
│
├── templates/                       # HTML templates for the web app
│   ├── index.html                   # Welcome page
│   └── home.html                    # Results page
│
├── app.py                           # Main Flask application script
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker file 
└── README.md                        # Project documentation

```
---
## Demo Video 
https://github.com/user-attachments/assets/7d673aef-ae1c-4bc9-a3d3-8bbcf116bdce

---
NOTE: This full-stack Gen-AI web application was previously deployed at a Public IP Address 54:198:93:248:8080 assigned by the AWS EC2 instance
