#     #!/usr/bin/env python
#     # coding: utf-8
############## Notes ###############################################
# #if we use multiple models, we can keep loop through them in the function
# #in folder, put the few-shot learning files so it can refer to it 
# #make a requirements.txt

# import module   
import subprocess
import os
import time 
import nbformat
import asyncio
#from openai import OpenAI

#dummy function 

######## TESTER TO TEST INTERFACE BC FUNCTION DOESN'T WORK YET ########

def function(input):
    #j returns file content
    content = "import streamlit as st\nst.button(\"Click me!\")"
    return content

def run_streamlit_dashboard(code):
    # Save the generated Streamlit code to a temporary file
    temp_filename = "temp_dashboard.py"
    with open(temp_filename, "w") as f:
        f.write(code)
    
    # Run the Streamlit app in the background using subprocess
    # `streamlit run` will execute the generated Streamlit code
    # env = os.environ.copy()
    # env["BROWSER"] = ""
    subprocess.Popen(['streamlit', 'run', temp_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Sleep for a few seconds to give Streamlit time to launch
    time.sleep(5)  # Give Streamlit some time to start up

    # Assuming the app runs locally on port 8501
    #port number may be am issue depending on device 
    return "http://localhost:8501"


# async def function(input_file):
#     await module._module.load('ollama')

#     get_ipython().system('pip install openai')

#     # Start a background process using subprocess.Popen
#     process = subprocess.Popen(['ollama', 'serve'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     nb_code = nbformat.read(input_file, as_version=4)
    
#     py_script = ''
#     for cell in nb_code['cells']:
#         if (cell['cell_type'] == 'code'):
#             py_script += cell['source'] + '\n'
#     py_script


#     client = OpenAI(
#         base_url = 'http://localhost:11434/v1',
#         api_key='ollama',
#     )

#     #CHANGE IF NEEDED IF WE DECIDE ON ONE
#     model= "gemma2:latest"


#     def prompt_with_examples(prompt, examples=[]):
#         full_prompt = prompt + "\n\n--- Examples ---\n\n"
        
#         # Append each example pair
#         for example_prompt, example_response in examples:
#             full_prompt += f"Example Prompt:\n{example_prompt}\nExample Response:\n{example_response}\n\n"
            
#         full_prompt += "\n--- End of Examples ---\n\n. Convert the following code to Streamlit code ONLY"
#         full_prompt += prompt
#         return full_prompt


#     def generate(system_prompt, examples, model):
#         # Prepare the messages for the API call
#         messages = [
#             {
#                 "role": "system",
#                 "content": system_prompt,
#             },
#             {
#                 "role": "user",
#                 "content": examples,
#             }
#         ]

#         # Call the chat completion API
#         response = client.chat.completions.create(
#             model=model,
#             messages=messages,
        
#         )

#         # Extract and return the generated content
#         return response.choices[0].message.content.strip()


#     # Example1
#     file_path = 'ratings.ipynb'
#     nb_code = nbformat.read(file_path, as_version=4)

#     example1_prompt = ''
#     for cell in nb_code['cells']:
#         if (cell['cell_type'] == 'code'):
#             example1_prompt += cell['source'] + '\n'

#     file_path = 'ratings.py'
#     with open(file_path, 'r') as file:
#         example1_ans = file.read()

#     # Example2
#     file_path = 'greetings-button.ipynb'
#     nb_code = nbformat.read(file_path, as_version=4)

#     example2_prompt = ''
#     for cell in nb_code['cells']:
#         if (cell['cell_type'] == 'code'):
#             example2_prompt += cell['source'] + '\n'

#     file_path = 'greetings-button.py'
#     with open(file_path, 'r') as file:
#         example2_ans = file.read()



#     # Example3
#     file_path = 'title-input.ipynb'
#     nb_code = nbformat.read(file_path, as_version=4)

#     example3_prompt = ''
#     for cell in nb_code['cells']:
#         if (cell['cell_type'] == 'code'):
#             example3_prompt += cell['source'] + '\n'

#     file_path = 'title-input.py'
#     with open(file_path, 'r') as file:
#         example3_ans = file.read()


#     # Example4
#     file_path = 'number-input.ipynb'
#     nb_code = nbformat.read(file_path, as_version=4)

#     example4_prompt = ''
#     for cell in nb_code['cells']:
#         if (cell['cell_type'] == 'code'):
#             example4_prompt += cell['source'] + '\n'

#     file_path = 'number-input.py'
#     with open(file_path, 'r') as file:
#         example4_ans = file.read()


#     system_prompt = "No syntax errors and complier errors.Streamlit code ONLY"
#     user_prompt = f"Only convert this Python code to Streamlit code using the Streamlit library:\n\n{py_script}\n\n"

#     examples = [
#         (example1_prompt, example1_ans),
#         (example2_prompt, example2_ans),
#         (example3_prompt, example3_ans),
#         (example4_prompt, example4_ans)
#     ]

#     structuredPrompt = prompt_with_examples(user_prompt, examples)

#     output = generate(system_prompt, structuredPrompt, model= model)
#     print(output)

#     start_index = output.find("```") + 3  # Move past the first '''
#     start_index = output.find("\n", start_index) + 1
#     substring = output[start_index:]  # Start from after the first '''

#     # Find the position of the second occurrence of '''
#     end_index = substring.find("```")  # Find the second '''

#     # Extract the substring between the first and second ''' (which is only the code part)
#     final_substring = substring[:end_index].strip()  # Remove any leading/trailing whitespace

#     # Output the desired substring (just the code)
#     print(final_substring)


# if __name__ == "__main__":
#     asyncio.run(function("input_notebook.ipynb"))





