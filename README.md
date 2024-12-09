# Axle-Informatics

## File Descriptions

### dashboard-convertion
- Examples from Axle CA's during data collection

### dataset
- 30 data examples gathered by student team 

### README.md 
- This document

### converter.ipynb
- Anika's working few-shot model as a notebook using nbformat convert 

### converter_func_maya.py
- Maya altered Anika's converter.ipynb to make it one function 
- There are some problems to be addressed 
- It's connected with the interface.py (streamlit application) 

### few-shot-learning.ipynb 
- Anika's previous version of converter.ipynb without using nbconvert (manual conversion to py script used instead)

### interface.py
- Maya's streamlit interface for users to use converter 
- Connected to cconverter_func_maya.py
- Runnable using 'streamlit run interface.py' in terminal if you want to see it!

### pipeline-exercide.ipynb
- Notebook given to practice modeling and prompting using models from OpenAI

### with_converter.ipynb 
- (not sure) 

### new.py
updated version of interface.py that lets the host link come up without openning tab automatically. 


# **Automated Dashboard Conversion Tool**  
*Axle Informatics AI Studio Challenge – Fall 2024*

---

## **Table of Contents**  
1. [Project Overview](#project-overview)  
2. [Business Impact](#business-impact)  
3. [Technical Approach](#technical-approach)  
4. [Key Features](#key-features)  
5. [Challenges and Insights](#challenges-and-insights)  
6. [Future Enhancements](#future-enhancements)  
7. [Acknowledgments](#acknowledgments)  

---

## **Project Overview**  
The **Automated Dashboard Conversion Tool** aims to leverage large language models (LLMs) to streamline the translation of Jupyter Notebooks into interactive Python dashboards. This innovation simplifies data visualization for researchers, statisticians, and engineers, enhancing collaboration and internal communication.

### **Objective**  
- Develop an LLM capable of converting notebook scripts into dashboard scripts using libraries like **Streamlit**.  
- Provide a user-friendly interface to facilitate the conversion process, allowing researchers to focus on insights rather than coding.

---

## **Business Impact**  
Axle Informatics operates at the intersection of bioinformatics and computational science. This project addresses:  
- **Efficiency**: Reducing the time and resources required to create dashboards.  
- **Accessibility**: Empowering non-coding researchers to utilize advanced data visualization tools.  
- **Innovation**: Advancing the integration of AI in the development of scientific tools.  

By automating the notebook-to-dashboard process, Axle can optimize internal workflows and extend this solution to broader industry applications.

---

## **Technical Approach**  

### **Data Preparation**  
- **Source**: Open-source Jupyter Notebooks (e.g., Kaggle, GitHub).  
- **Structure**: Input notebooks with visualizations (plots, graphs) and their corresponding dashboard scripts.  
- **Preprocessing**:  
  - Convert `.ipynb` files to `.py` scripts.  
  - Ensure consistency in syntax, formatting, and metadata.  
  - Aggregate inputs and outputs into a labeled dataset for model training.  

### **Modeling**  
- **Techniques Used**:  
  - In-context learning with few-shot examples.  
  - Retrieval-Augmented Generation (RAG).  
  - Fine-tuning pre-trained LLMs (e.g., deepseek-coder-v2:16b).  
- **Validation**:  
  - Developed a scoring rubric to assess code quality, functionality, and design.  

### **Tools and Platforms**  
- **Programming**: Python, JupyterLab, Streamlit.  
- **Collaboration**: Notion, GitHub, Google Colab.  
- **Resources**: Kaggle datasets, Streamlit documentation, and Axle-provided tools.

---

## **Key Features**  
- **Interactive Interface**:  
  Converts notebooks to dashboards and provides downloadable outputs.  
- **Streamlit Integration**:  
  Currently supports **Streamlit dashboards** exclusively.  

---

## **Challenges and Insights**  
### **Challenges**  
- Balancing output accuracy with time constraints.  
- Handling variations in notebook structures and coding styles.  
- Mitigating issues in model prompting and syntax errors.  

### **Insights**  
- Splitting tasks and consistent communication enhanced efficiency.  
- Few-shot learning is effective for targeted model training.  
- Iterative refinement ensures model robustness and quality output.

---

## **Future Enhancements**  
- Expand support to other dashboarding libraries, such as **Dash** and **Shiny**.  
- Develop a fully functional user interface for easier interaction.  
- Implement **automated quantitative scoring** to evaluate the accuracy and quality of visual outputs from different models.  
- Enable real-time conversion with improved LLM deployment.  
- Add a preview functionality for users to verify dashboard visuals before download.

---

## **Acknowledgments**  
We express our gratitude to:  
- **Advisors**: Aditi Patel, Konstantin Taletskiy, and Jesse Ward for their mentorship and feedback. This project would not be a success without you all.  
- **Axle Informatics**: For sponsoring this project and providing invaluable resources.  
- **AI Studio Program**: For fostering collaboration and innovation.  

### **Team Members**  
- Anika Guin  
- Maya Patel  
- Zeynep Alta  

---


