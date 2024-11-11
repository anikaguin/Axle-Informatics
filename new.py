import streamlit as st
from converter_func_maya import function, run_streamlit_dashboard #for dummy func testing


st.header("Dashboard Converter")
st.subheader("Convert a notebook file (.ipynb) into a Streamlit Dashboard to enhance visualization!")

#to enable button
if "condition_met" not in st.session_state:
    st.session_state.condition_met = False

#dropdown for selecting file? upload file
uploaded_file = st.file_uploader("Upload a .ipynb notebook file", type="ipynb")
#check if file is correct type 

if uploaded_file is not None:
    #check is ipynb 
    if not(uploaded_file.name.endswith(".ipynb")):
        st.write("Wrong file type. Provide a notebook file (.ipynb)")
    #if yes, do conversion.
    else:
        st.session_state.condition_met = True
        if st.button("Convert"):
            with st.spinner("Creating visualization..."):
                dashboard = function(uploaded_file)
            st.download_button(label = "Download", data = dashboard, file_name = 'dashboard.py', 
                               mime = "text/python")   
            #if st.button("Click here to view your dashboard"): 
            with st.spinner("Creating visualization..."):                  
                dashboard_url = run_streamlit_dashboard(dashboard)
                st.markdown(dashboard_url, unsafe_allow_html=True )
            

#visualize 



# '''TIPS for later'''
# display code using 

# with st.echo():
#     st.write("code will be executed and printed")

# add a progress spinner if needed while the LLM loads 