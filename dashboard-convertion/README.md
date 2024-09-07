# Example of converting a Jupyter notebook to a Streamlit app

We'll use the following AI tools:
- Claude Sonnet 3.5
- OpenAI GPT-4o
- Llama 2.0


1. Create working environment using Conda:

```
conda create -n dashboard-conversion -c conda-forge python=3.12 jupyterlab=4.2 ipywidgets matplotlib plotly altair streamlit
```

2. Activate the environment:

```
conda activate dashboard-conversion
```

3. Convert the Jupyter notebook to a Python script:

```
jupyter nbconvert --to script population-dashboard-notebook.ipynb --output population-dashboard-script
```