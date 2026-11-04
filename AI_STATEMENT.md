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

**AI Assistance (`src/thermodynamics.py`, `test/test_thermodynamics.py`)**

**TOOL USED:** ChatGPT (OpenAI)

**PROMPT:** Questions about cumulative probability, entropy calculations, Python functions and testing.

**AI-GENERATED SUGGESTION:** Use a `for` loop in `cumulative_probability()` to sum probabilities over an interval and `math.log()` in `entropy_change()` to apply Boltzmann's equation. ChatGPT also suggested using `math.isclose()` for numerical tests and reusing functions from `combinatorics.py`.

**PURPOSE OF THE SUGGESTION:** To implement and verify the probability and entropy calculations for Part 2 (a–g).

**UNDERSTANDING AND MODIFICATIONS:** I reviewed the  functions, adapted them to the code and removed duplicated lines. I understood how the probability sum and entropy difference were obtained and checked the results in Google Colab. 
