"""
Microstates enumeration for a system of N coins
Each coin can be heads(1) or tails (0)
"""
def generate_microstates(N:int): 
  """
  It generates all possible microstates for N coins
  It returns
    A list of binary strings, where 0 represents tails and 1 represents heads
  """
  if N<=0:
    raise ValueError ("N must be greater than 0")
  microstates=[]
  for i in range(2**N):
    state=format(i,f"0{N}b")
    microstates.append(state)
  return microstates

def count_heads():
