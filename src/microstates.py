"""
Microstates enumeration for a system of N coins
Each coin can be heads(1) or tails (0)
"""
def generate_microstates(N): 
  """
  It generates all possible microstates for N coins
  It returns
    A list of binary strings, where 0 represents tails and 1 represents heads
  """
  if N<=0:
    raise ValueError ("N must be greater than 0")
  microstates_list=[]
  for i in range(2**N):
    microstate=format(i,f"0{N}b")
    microstates_list.append(microstate)  
  return microstates_list

def count_heads(microstate):
  """
  Counts the number of heads (1) in the microstate.
  """
  for bit in microstate:
    if bit!="0" and bit !="1":
      raise ValueError ("A microstate can only contain 0 and 1")
  return microstate.count("1")


def group_by_heads(microstates_list):
  """
  Group microstates according to the number of heads
  """
  N=len(microstates_list[0]) 
  "We need the number of bits that conform the microstates to know how many grops we should obtain"
  groups={}
  for k in range(N+1):
    groups[k]= []
  for microstate in microstates_list:
    k=count_heads(microstate)
    groups[k].append(microstate)
  return groups


