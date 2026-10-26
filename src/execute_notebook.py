"""
execute_notebook.py
-------------------
Executes notebooks/food_delivery_prediction.ipynb using nbclient
and saves the notebook populated with outputs and plots.
"""

import os
import nbformat
from nbclient import NotebookClient

def run_nb():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    nb_path = os.path.join(base_dir, "notebooks", "food_delivery_prediction.ipynb")
    print(f"Reading notebook from: {nb_path}")
    
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    client = NotebookClient(
        nb, 
        timeout=1200, 
        kernel_name="python3", 
        resources={"metadata": {"path": os.path.join(base_dir, "notebooks")}}
    )
    
    print("Executing all cells in notebook...")
    client.execute()
    
    with open(nb_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
        
    print(f"Notebook successfully executed and saved with outputs to: {nb_path}")

if __name__ == "__main__":
    run_nb()
