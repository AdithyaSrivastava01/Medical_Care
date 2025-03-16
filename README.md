# MedQuery AI: AI-Powered Medical Query Assistant (RAG-Based Web App)

This project leverages a Retrieval-Augmented Generation (RAG)-based web application that answers medical-related queries accurately. The system ingests knowledge from a medical book titled *The GALE ENCYCLOPEDIA of MEDICINE SECOND EDITION*, enabling it to generate informed and reliable responses. The project implements an LLM-based retrieval and contextual augmentation to enhance accuracy. The application ensures efficient query resolution and improves medical information accessibility through a user-friendly web interface. 

---

## Features  

- **Medical Query Assistant**: Implements a RAG-based approach to answer the medical queries provided by the user
- **Gen-AI interface**: Incorporate cloud-based vector database Pinecone coupled with HuggingFace sentence transformers for Embedding and OpenAI API for LLM integration into the application. 
- **User-Friendly Web Application**: Developed using Flask, HTML, and CSS for real-time answers.  
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
Medical_Care/
│
├── research/
│   └── new_research.ipynb           # Investigations
│                   
├── src/                             # Main scripts
│   ├── __init__.py                  # Initialization of the objects
│   ├── helpers.py                   # Helper functions for text chunking and embedding the documents
│   └── prompt.py                    # Prompt Engineering Template for the LLM
│
├── static/
│   └── style.css                    # CSS file that includes the styling of the Web page
│ 
├── templates/                       # HTML templates for the web app
│   └── chatbot.html                 # Chatbot Web Page
│
├── .gitignore
├── app.py                           # Main Flask application script
├── setup.py                         # Python script to publish the Python Package
├── template.py                      # Template Python Script to automate the process of creating the project file structure
├── store_index.py                   # Used to create a store_index in Pinecone and store the vector Embedding
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker file 
└── README.md                        # Project documentation

```
---
## Demo Video 
https://github.com/user-attachments/assets/7d673aef-ae1c-4bc9-a3d3-8bbcf116bdce

---
NOTE: This full-stack Gen-AI web application was previously deployed at a Public IP Address 54:198:93:248:8080 assigned by the AWS EC2 instance
