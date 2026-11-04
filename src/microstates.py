"""
Microstates enumeration for a system of N coins
Each coin can be heads(H) or tails (T)
"""
def generate_microstates(N): 
  """
  It generates all possible microstates for N coins
  It returns
    A list of strings, where H represents tails and T represents heads
  """
  if N<=0:
    raise ValueError ("N must be greater than 0")
  microstates_list=[]
  for i in range(2**N):
    microstate=format(i,f"0{N}b")
    microstate = microstate.replace("0", "T").replace("1", "H")
    microstates_list.append(microstate)  
  return microstates_list

def count_heads(microstate):
  """
  Counts the number of heads (1) in the microstate.
  """
  for bit in microstate:
    if bit!="H" and bit !="T":
      raise ValueError ("A microstate can only contain H and T")
  return microstate.count("H")


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


