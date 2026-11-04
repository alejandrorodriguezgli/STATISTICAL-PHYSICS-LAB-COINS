

**AI Assistance Microstate Enumeration: max number(notebooks/max_N.ipynb)**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I asked chatGPT what function I had to use to measure the memory used

AI- GENERATED SUGGESTION: 
import tracemalloc  

PURPOSE OF THE SUGGESTION: insert the function in the code using:tracemalloc.start(), tracemalloc.get_traced_memory(),tracemalloc.stop()

UNDERSTANDING AND MODIFICATIONS:  it is a fucntion that starcs tracking the memory used with tracemalloc.start() and whith tracemalloc.get_traced_memory() it returns a tuple containing two integer values in bytes: the current memory being used at that exact moment and the maximum peak memoy used since trackins started. And finally tracemalloc.stop() ends the memory tracking and clears the recorded trace data. With this information, I included it in my function.


**AI Assistance Microstate Enumeration: max number(notebooks/max_N.ipynb)**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I have an error when running the cell, it does not find the folder src where the function generate_micrsotates is

AI- GENERATED SUGGESTION:   
import os  
os.chdir("..")

PURPOSE OF THE SUGGESTION: the problem is that VS Code and Pyhton do not start in teh same code. When running the notebook, the directory where Python is working is in notebooks, but the src folder is one level above notebooks, Pyhton is looking for src inside notebooks. With this function we indicate Python to move one folder up.

UNDERSTANDING AND MODIFICATIONS: I understood the function and add it to the beginning of the code, I left it as it is becuase I could not came up with another solution
