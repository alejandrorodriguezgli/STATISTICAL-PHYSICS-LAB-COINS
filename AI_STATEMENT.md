**AI Assistance Combinatorics: omega and log_omega (src/combinatorics.py, test/test_combinatorics.py)**
TOOL USED: Claude (Anthropic)

PROMPT: I asked Claude for help with coding logic regarding the omega and the log_omega functions, so that they could work effectively.

AI-GENERATED SUGGESTION: Assisted me with the coding for each, like how we compute omega using the binomial coefficient in another form and the symmetry k = min(k, N-k). In addition, it helped me understand how pytest and parametrize work for the testing part.

PURPOSE OF THE SUGGESTION: Computing Omega(N, k) without calculating huge factorials and computing log_Omega for large N without overflow.

UNDERSTANDING AND MODIFICATIONS: I asked Claude to explain each part step by step, how (N - k)! cancels from N!/(k!(N-k)!) and why k = min(k, N-k) reduces the number of steps. I wrote comments in the code with my own words, to make sure I understood the whole process while explaining the logic I wrote with some help. Also, I fixed some problems like the misplaced code and some wrong comments. 

TESTS: Since these functions were written with the help of AI, I added unit tests with pytest to verify them:
- test_omega_matches_math_comb: omega gives the same values as Python's math.comb for N = 1, 5, 20, 100 and 500.
- test_symmetry: Omega(100, k) = Omega(100, 100-k) for every k.
- test_impossible_k: impossible k values give 0 microstates in omega and -infinity in log_omega.
- test_log_omega_matches_exact: log_omega agrees with the logarithm of the exact integer omega for N = 10, 100 and 1000 
All of them pass.

**AI Assistance Combinatorics: distribution and probability (src/combinatorics.py, test/test_combinatorics.py)**
TOOL USED: Claude (Anthropic)

PROMPT: I consulted Claude when creating the functions distribution and probability. 

AI-GENERATED SUGGESTION: It helped me with a small error with the distribution function since it didn't compile and assisted me building the probability function in log-space so it never overflows.

PURPOSE OF THE SUGGESTION: Getting the full distribution for the plots of Part 1 right and computing the probability without overflow.

UNDERSTANDING AND MODIFICATIONS: After talking with Claude I understood my mistakes and why we use logarithms to assure we get small decimal numbers so that the program doesn't overflow, even though they come with a small error. I also wrote many comments.

TESTS: Since these functions were written with AI, I also tested them with pytest:
- test_table_n7: distribution(7) gives 1, 7, 21, 35, 35, 21, 7, 1, the table of Part 1 (a).
- test_total_microstates: the sum of the distribution equals 2^N for N = 0, 1, 7, 50 and 100.
- test_probabilities_sum_to_one: the probabilities add up to 1 for N = 1, 20, 100 and 1000.
All of them pass.

**AI Assistance Maximum N and timings (notebooks/max_N.ipynb)**
TOOL USED: Claude (Anthropic)

PROMPT: I asked Claude how measure the computation time of the distribution as N grows, as I wasn't sure how to structure my loop.

AI-GENERATED SUGGESTION: Timing each N five times with t0 = time.perf_counter() and times.append(time.perf_counter() - t0).

PURPOSE OF THE SUGGESTION: Calculating the average of time for each computation.

UNDERSTANDING AND MODIFICATIONS: I understood the loop and the method to get the times correctly. After that I added some comments and 
used mean and std to get the final values.

**AI Assistance Extra figure for Part 1 (e) (src/combinatorics.py: plot_probabilities, report/figures/probability_narrowing.pdf)**
TOOL USED: Claude (Anthropic)

PROMPT: I was trying to understand the Gaussian in (e).

AI-GENERATED SUGGESTION: The AI suggested I should do a graph showing the probability versus fraction of heads k/N, in order to show the peak gets narrower as N grows. It also suggested how I could build it using a loop.

PURPOSE OF THE SUGGESTION: Showing visually that the peak at k/N = 0.5 gets narrower and taller as N grows, which supports the conclusion that for N ~ 10^23 the distribution forms a spike.

UNDERSTANDING AND MODIFICATIONS: I thought it was a good idea, implemented the plot and added it to the explanation in (e).

