
# **Automated Dashboard Conversion Tool**  
*Axle Informatics AI Studio Challenge – Fall 2024*

---

## **Table of Contents**  
1. [Project Overview](#project-overview)
2. [Objective](#objective) 
3. [Business Impact](#business-impact)  
4. [Methodology](#methodology)  
5. [Key Features](#key-features)  
6. [Results and Key Findings](#results-and-key-findings)
7. [Visualizations](#visualizations)
8. [Potential Next Steps](#potential-next-steps)  
9. [Acknowledgments](#acknowledgments)
10. [Individual Contributions](#individual-contributions)
11. [File Descriptions](#file-descriptions)
12. [How to Run It](#how-to-run-it)

---

## **Project Overview**  
The **Automated Dashboard Conversion Tool** aims to leverage large language models (LLMs) to streamline the translation of Jupyter Notebooks into interactive Python dashboards. This innovation simplifies data visualization for researchers, statisticians, and engineers, enhancing collaboration and internal communication.

### **Objective**  
- Automate the notebook-to-dashboard translation process.  
- Develop an LLM capable of converting notebook scripts into dashboard scripts using libraries like **Streamlit**.  
- Provide a user-friendly interface to facilitate the conversion process, allowing researchers to focus on insights rather than coding.
- Provide a scalable framework adaptable to multiple dashboarding libraries.
---

## **Business Impact**  
Axle Informatics operates at the intersection of bioinformatics and computational science. This project addresses:  
- **Efficiency**: Reducing the time and resources required to create dashboards.  
- **Accessibility**: Empowering non-coding researchers to utilize advanced data visualization tools.  
- **Innovation**: Advancing the integration of AI in the development of scientific tools.  

By automating the notebook-to-dashboard process, Axle can optimize internal workflows and extend this solution to broader industry applications.

---

## **Methodology**  

### **Data Preparation**  
- **Source**: Open-source Jupyter Notebooks (e.g., Kaggle, GitHub).  
- **Structure**: Input notebooks with visualizations (plots, graphs) and their corresponding dashboard scripts.  
- **Preprocessing**:  
  - Convert `.ipynb` files to `.py` scripts.  
  - Ensure consistency in syntax, formatting, and metadata.  
  - Aggregate inputs and outputs into a labeled dataset for model training.  

### **Modeling**  
- **Techniques Used**:
  - Incorporated **few-shot learning** to guide the model using prompt examples.  
  - Used Retrieval-Augmented Generation (RAG) to enhance model capabilities.  
  - Fine-tuning pre-trained LLMs (e.g., deepseek-coder-v2:16b).
    
- **Validation**:  
  - Developed a scoring rubric to assess code quality, functionality, and design.
  - Employed scoring rubrics for quantitative evaluation.

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

## **Results and Key Findings**  

### **Results**  
- Successfully implemented a model to convert Jupyter Notebook scripts into **Streamlit** dashboard scripts.  
- Achieved high accuracy in dashboard functionality and code clarity.

### **Challenges**  
- Balancing output accuracy with time constraints.  
- Handling variations in notebook structures and coding styles.  
- Mitigating issues in model prompting and syntax errors.  

### **Key Findings**  
- Splitting complex tasks and iterative refinement improved output quality.  
- Prompting is crucial in steering LLM behavior for specific use cases.  
- Current implementation is limited to Streamlit dashboards but demonstrates potential for scaling.

---

## **Visualizations**  
- **Code Conversion Outputs**: Demonstrated with examples of translated notebooks and corresponding dashboards.  
- **Process Flow Diagram**: Showcasing data preparation, modeling, and validation steps.  
- **Dashboard Snapshots**: Highlighting the resulting interactive visualizations.

---

## **Potential Next Steps**  
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

## **Individual Contributions**  

### **Anika Guin**  
- Managed the implementation of dashboarding techniques with Streamlit.
- Contributed to documentation and presentation development.
- Led the modeling approach and refined prompting techniques with few-shot learning.
- Gathered and created at least 10 dataset examples.
- Initiated interface for conversions.

### **Maya Patel**  
- Managed the implementation of dashboarding techniques with Streamlit.
- Contributed to documentation and presentation development.
- Led the modeling approach and refined prompting techniques with few-shot learning.
- Gathered and created at least 10 dataset examples.
- Advanced interface application to working status.

### **Zeynep Alta**  
- Managed the implementation of dashboarding techniques with Streamlit.  
- Contributed to documentation and presentation development.
- Managed Notion and generated documentation for group. 
- Gathered and created at least 10 dataset examples.
- Oversaw data validation and scoring rubric design.
- Debugged interface application.

---

## **File Descriptions**

### dashboard-convertion
- Examples from Axle CA's during data collection

### dataset
- 30 data examples gathered by student team 

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

### new.py
- Updated version of interface.py that lets the host link come up without openning tab automatically. 

---

## **How to Run It**  
1. **Download the Jupyter Notebook**: The notebook containing the function can be downloaded from the repository.  
2. **Ensure GPU Availability**: Run the notebook on a platform with GPU support, such as Notebooks Hub or Google Colab. This is necessary to run the Ollama tool for the model.
    - **Using Notebooks Hub**:  
        - Log in and create a new server with GPU enabled.  
        - Choose **JupyterLab** or **VS Code** as your interface.  
        - Clone the repository and open the notebook for execution.  
3. **Install Dependencies**: Ensure that all required libraries (e.g., `streamlit`, `ipywidgets`) are installed.  
    - Use the following commands in a terminal:  
      ```
      pip install -r requirements.txt
      ```
4. **Run the Notebook**: Follow the instructions in the notebook to execute the code and generate Streamlit dashboards.  

---
