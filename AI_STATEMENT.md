**AI Assistance Microstate Enumeration: max number(notebooks/max_N.ipynb)**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I asked chatGPT which function I had to use to measure the memory required by generate_microstates() function 

AI- GENERATED SUGGESTION:  
import psutil  
process = psutil.Process(os.getpid())  
process.memory_info().rss  


PURPOSE OF THE SUGGESTION: measuring the Pyhton memory consumption when generating and storing all possible microstates for a given number of coins N.  

UNDERSTANDING AND MODIFICATIONS:  
import psutil: library that provides information aboutr running processes  
process = psutil.Process(os.getpid()):  
process.memory_info().rss: obtains the Resident Set Size (RSS), that represents the physical RAM occupied by the Python process.   
After understanding it, I included it to obtain the memory consumed: by computing the memory occupied just at the beinning and just at the end and subtracting them, we obtain the memory consumed in the process.

**AI Assistance Microstate Enumeration: max number(notebooks/max_N.ipynb)**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I asked chatGPT what function I had to use to empty the memory after each iterations to prevent the memory used in previously generated micsrostates from accumulating during subsequent tests 

AI- GENERATED SUGGESTION: 
del microstates
gc.collect()



## Member 3 – Probability and Entropy

**TOOL USED:** ChatGPT (OpenAI)

**PROMPTS USED:**
how to include both limits in cumulative_probability() 
how to test probability calculations and not gettin errors due to numerical precision
how to calculate entropy differences in entropy_change() using the multiplicities of two macrostates

**AI-GENERATED SUGGESTION:** 
ange(k1, k2 + 1) to include both limits
`math.isclose()` for floating-point comparisons, import existing functions and preserve both contributions. 
math.log() to calculate entropy
**PURPOSE:** To improve the tests and integrate the code with the rest of the project.

**UNDERSTANDING AND MODIFICATIONS:** I updated the tests, removed duplicated functions and checked the calculations in Google Colab.
