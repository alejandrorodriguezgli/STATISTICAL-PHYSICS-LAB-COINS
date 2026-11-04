
**AI Assistance Microstate Enumeration: src/microstates.py**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: how can I check if N is a valid input before starting computing the microstates?

AI- GENERATED SUGGESTION:   
if not isinstance(N, int) or isinstance(N, bool):

PURPOSE OF THE SUGGESTION: not isinstance(N, int) checks if N is not an integer and isinstance(N, bool) checks if N is not a boolian.

UNDERSTANDING AND MODIFICATIONS: if the values id not an integer or if it is a boolian the error ValueError("N must be a positive integer") raises. I added the condition or N<0 so that the complete line of code was finally:  
if not isinstance(N, int) or isinstance(N, bool) or N <= 0:  
--raise ValueError("N must be a positive integer")


**AI Assistance Microstate Enumeration: src/microstates.py**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I have an error when running the cell, it does not find the folder src where the function generate_micrsotates is

AI- GENERATED SUGGESTION:   
import os  
os.chdir("..")

PURPOSE OF THE SUGGESTION: the problem is that VS Code and Pyhton do not start in teh same code. When running the notebook, the directory where Python is working is in notebooks, but the src folder is one level above notebooks, Pyhton is looking for src inside notebooks. With this function we indicate Python to move one folder up.

UNDERSTANDING AND MODIFICATIONS: I understood the function and add it to the beginning of the code, I left it as it is becuase I could not came up with another solution

**AI Assistance Microstate Enumeration: src/microstates.py**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I asked chatGPT how to write the string of the microstate

AI- GENERATED SUGGESTION: 
format(i, f"0{N}b")

PURPOSE OF THE SUGGESTION: it converts an integer (i) into a binary string with exactly N digits.

UNDERSTANDING AND MODIFICATIONS:  I implemented this and then I add microstate = microstate.replace("0", "T").replace("1", "H") to obtain the strings with letters so that we could identify heads or tails easier.

**AI Assistance Microstate Enumeration: max number(notebooks/max_N.ipynb)**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: I asked chatGPT what function I had to use to measure the memory used

AI- GENERATED SUGGESTION: 
import tracemalloc  

PURPOSE OF THE SUGGESTION: insert the function in the code using:tracemalloc.start(), tracemalloc.get_traced_memory(),tracemalloc.stop()

UNDERSTANDING AND MODIFICATIONS:  it is a fucntion that starcs tracking the memory used with tracemalloc.start() and whith tracemalloc.get_traced_memory() it returns a tuple containing two integer values in bytes: the current memory being used at that exact moment and the maximum peak memoy used since trackins started. And finally tracemalloc.stop() ends the memory tracking and clears the recorded trace data. With this information, I included it in my function.

**AI Assistance Microstate Enumeration: report_part1.txt)**  
TOOL USED: ChatGPT (OpenAI)  

PROMPT: give me this tables in LaTex code ( and I introduced the tables of all possible microstates for N=7, the table with the data of: the memory, time, all microstates and the maxium number of N, and also the data of the table of the number of microstates for each possible number of headstable in N=/ 

AI- GENERATED SUGGESTION: it gave me the tables in Latex code


PURPOSE OF THE SUGGESTION: insert the function in the code using:tracemalloc.start(), tracemalloc.get_traced_memory(),tracemalloc.stop()

UNDERSTANDING AND MODIFICATIONS:  it is a fucntion that starcs tracking the memory used with tracemalloc.start() and whith tracemalloc.get_traced_memory() it returns a tuple containing two integer values in bytes: the current memory being used at that exact moment and the maximum peak memoy used since trackins started. And finally tracemalloc.stop() ends the memory tracking and clears the recorded trace data. With this information, I included it in my function.



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

AI Assistance Thermodynamic implications: waiting time and likelihood ratio (src/thermodynamics.py, tests/test_part4.py)

TOOL USED: Claude (Anthropic)
PROMPT: I asked Claude to check my code and check that the functions for Part 2 (h) and (i) were reusing the exact same functions log_omega and omega that my teammate had already written in combinatorics.py were well integrated.

AI-GENERATED SUGGESTION: Claude check my code and suggested implementing log10_waiting_time for (h), and orientated me in how to implement correctly and more efficiently the likelihood_ratio for (i). With this, the waiting time is compted as 1/P_8 = 2^N / Omega(N, 8) and returned as a base-10 logarithm, and the ratio P(N/2)/P(N/2 ± 10) is computed as a difference of logarithms because the factor 2^N cancels, so those suggestions where pretty useful.

PURPOSE OF THE SUGGESTION: to get numbers that are far too big for a normal float without overflow, and expressing them in a more interpreted way

UNDERSTANDING AND MODIFICATIONS: I asked Claude to explain why the waiting time is 1/P. Each second the N coins are tossed once, which is an independent trial that succeeds (exactly 8 heads) with probability P_8. The number of trials until the first success follows a geometric distribution, whose mean is 1/P_8, in the same way that you need on average 6 rolls of a die to get a 6. In the ratio, both probabilities are divided by the same 2^N, so it cancels, and by the symmetry k <-> N-k the result is the same for N/2+10 and N/2-10. My part of the code and its functions were added at the end of my teammate's thermodynamics.py instead of creating a new file, to avoid merge conflicts in GitHub (as happened several times before)

TESTS: Since these functions were highly written with AI, I verified them with pytest:

* test_waiting_time_matches_exact_integers: the log-space waiting time for N = 113 agrees with the exact value computed with Python integers.
* test_likelihood_ratio_log_vs_exact: the ratio computed with logarithms agrees with the exact integer ratio for N = 100, 113 and 150, and is always greater than 1. All of them pass.

AI Assistance Large N limit (src/thermodynamics.py, tests/test_part4.py)

TOOL USED: ChatGPT (OpenAI)
PROMPT: I asked why lgamma gives absurd results for N ~ 10^23 even though it works and there is no overflow.

AI-GENERATED SUGGESTION: it explained that log_omega (based on math.lgamma) stops being accurate for such N […]. It wrote large_n_summary, which re-evaluates questions (a)–(i) for N = 10^23 using Stirling’s approximation instead of lgamma.

PURPOSE OF THE SUGGESTION: Obtaining meaningful values in the thermodynamic limit.

UNDERSTANDING AND MODIFICATIONS: A float keeps about 16 significant digits, so a number like lnGamma(10^23) ~ 5·10^24 already has a rounding error of order 10^9; when the large terms cancel, what is left is dominated by that error. Stirling's approximation gives the logarithm of the multiplicity directly as a Gaussian and becomes more accurate as N grows.

TESTS:

* test_large_N_limit: for N = 10^23 the relative width is 1/sqrt(N), a window of ±10 coins has negligible probability and ΔS(g)/k_B ≈ N ln 2. It pass.

AI Assistance Conceptual questions

TOOL USED: Claude (Anthropic)
PROMPT: I use it to understand the tools and the organisation of the project, like what Conda, VS code studio and GitHub are and what each file of the project is for, how to install and setup everything, whether cloning the repository could expose my other folders… etc, as well as some conceptual questions like why N/2 is the most probable macrostate, why the distribution narrows as 1/sqrt(N), as well as some technical questions regarding the use of Github (as I had never used it before), especially with git branches and merge conflicts.

AI-GENERATED SUGGESTION: Explanations for each question.

PURPOSE OF THE SUGGESTION: Understanding the workflow, solving theoretical doubts and also technical problems.

UNDERSTANDING AND MODIFICATIONS: Better approach for the general understanding of both the project and the set up of everything needed.


