**AI Assistance Microstate Enumeration(src/microstate.py)**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I asked chatGPT how to code the return statement of the generate_microstates(N) function, whcih should generate all possible microstates for a ssyem of N coins.  

AI- GENERATED SUGGESTION: return [format(i, f"0{N}b") for i in range(2**N)]  

PURPOSE OF THE SUGGESTION: that formula converts all integers from 0 to 2^(N-1) into a binary of N digits and collects all the values as  strings in a list. Ecah binary number represent a possible microstate (0 are tails and 1 are heads).  

UNDERSTANDING AND MODIFICATIONS: I asked ChatGPT to explain the expression step by step and when I undertsood it I chose an equivalent version written by me that includes a loop before the return:  

  microstates_list=[ ]  
  for i in range(2**N):  
  --microstate=format(i,f"0{N}b")  
  --microstates_list.append(microstate)  
  return microstates_list

**AI Assistance Microstate Enumeration: max number(notebooks/max_N.ipynb)**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I asked chatGPT what function I had to use to measure the memory required by generate_microstates() function 

AI- GENERATED SUGGESTION:  
import tracemalloc  
tracemalloc.start()  
microstates = generate_microstates(N)  
current_memory, peak_memory = tracemalloc.get_traced_memory()  
tracemalloc.stop()  

PURPOSE OF THE SUGGESTION: measuring the Pyhton memory consumption when generating and storing all possible microstates for a given number of coins N.  

UNDERSTANDING AND MODIFICATIONS: I asked to expolain me every step:start() begins memory tracking, get_traced_memory() it gives two values: current_memory that tells how much memory Python is using at that moment, and peak_memory that tells the  latgest amount of memory Python has used since tracking started. stop() ends tracking. I used this explanation to understand how the function works and integrat it in  my function: measure_microstate_memory(N_values)

**AI Assistance Microstate Enumeration: max number(notebooks/max_N.ipynb)**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I asked chatGPT what function I had to use to empty the memory after each iterations to prevent the memory used in previously generated micsrostates from accumulating during subsequent tests 

AI- GENERATED SUGGESTION: 
idel microstates
gc.collect()

PURPOSE OF THE SUGGESTION: with these two function you can relaes memory after each iteration

UNDERSTANDING AND MODIFICATIONS: del microstates delates the variable carrying the microstates list and gc.collect() requests Python to identify and clean unused objects. With this explanation I knew I had to place these tho function inside my for loop of my measure_microstate_memory(N_values) function so that they after  each iteration.


**AI Assistance Microstate Enumeration: max number(notebooks/max_N.ipynb)**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I have an error when running the cell, it does not find the folder src where the function generate_micrsotates is

AI- GENERATED SUGGESTION:   
import os  
os.chdir("..")

PURPOSE OF THE SUGGESTION: the problem is that VS Code and Pyhton do not start in teh same code. When running the notebook, the directory where Python is working is in notebooks, but the src folder is one level above notebooks, Pyhton is looking for src inside notebooks. With this function we indicate Python to move one folder up.
UNDERSTANDING AND MODIFICATIONS: I understood the function and add it to the beginning of the code, I left it as it is becuase I could not think of another solution
