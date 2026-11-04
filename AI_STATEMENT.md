

**AI Assistance Microstate Enumeration: max number(notebooks/max_N.ipynb)**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I asked chatGPT what function I had to use to empty the memory after each iterations to prevent the memory used in previously generated micsrostates from accumulating during subsequent tests 

AI- GENERATED SUGGESTION: 
del microstates
gc.collect()

PURPOSE OF THE SUGGESTION: with these two function you can release memory after each iteration

UNDERSTANDING AND MODIFICATIONS: del microstates delates the variable carrying the microstates list and gc.collect() requests Python to identify and clean unused objects. With this explanation I knew I had to place these tho function inside my for loop of my measure_microstate_memory(N_values) function so that they after  each iteration.


**AI Assistance Microstate Enumeration: max number(notebooks/max_N.ipynb)**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I have an error when running the cell, it does not find the folder src where the function generate_micrsotates is

AI- GENERATED SUGGESTION:   
import os  
os.chdir("..")

PURPOSE OF THE SUGGESTION: the problem is that VS Code and Pyhton do not start in teh same code. When running the notebook, the directory where Python is working is in notebooks, but the src folder is one level above notebooks, Pyhton is looking for src inside notebooks. With this function we indicate Python to move one folder up.

UNDERSTANDING AND MODIFICATIONS: I understood the function and add it to the beginning of the code, I left it as it is becuase I could not came up with another solution
