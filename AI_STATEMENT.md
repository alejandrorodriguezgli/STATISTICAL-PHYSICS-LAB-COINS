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



**AI Assistance in Probability and Entropy Calculations**  

**TOOL USED:** ChatGPT (OpenAI)

**PROMPTS:**

How can I include both limits in `cumulative_probability()`?

How can I avoid numerical precision errors when testing probabilities?

How can I calculate entropy differences in `entropy_change()` using the multiplicities of two macrostates?

**AI-GENERATED SUGGESTION:**

 `range(k1, k2 + 1)` to include both limits, `math.isclose()` for floating-point comparisons and `math.log()` to calculate entropy.

**PURPOSE OF THE SUGGESTION:**

To implement and test the probability and entropy calculations.

**UNDERSTANDING AND MODIFICATIONS:**

`range(k1, k2 + 1)` includes both limits since Python excludes the last value in `range()`.

`math.isclose()` allowes to compare numerical results while allowing small differences

`math.log()` calculates the logarithm of the multiplicity, which is needed in Boltzmann's equation.

