"""
Microstates enumeration for a system of N coins
Each coin can be heads(H) or tails (T)
"""
def generate_microstates(N): 
  """
  Generates all possible microstates for N coins using a generator.
   Returns:
        A generator that yields strings where H represents heads
        and T represents tails.
  """
  if not isinstance(N, int) or isinstance(N, bool) or N <= 0:
    raise ValueError("N must be a positive integer")
  
  for i in range(1 << N):
        microstate = format(i, f"0{N}b")
        microstate = microstate.replace("0", "T").replace("1", "H")
        yield microstate

def count_heads(microstate):
  """
  Counts the number of heads (H) in the microstate.
  """
  for bit in microstate:
    if bit not in("H", "T"):
      raise ValueError ("A microstate can only contain H and T")
  return microstate.count("H")


def group_by_heads(input_microstates):
  """
  Group microstates according to the number of heads
  """
  microstates_list=list(input_microstates)
  if not microstates_list:
    raise ValueError("The microstate list can not be empty")

  N=len(microstates_list[0]) 
  "We need the number of bits that conform the microstates to know how many grops we should obtain"
  
  groups={}
  for k in range(N+1):
    groups[k]= []
  
  for microstate in microstates_list:
    if len(microstate) != N:
      raise ValueError("All microstates must have the same length")
    k=count_heads(microstate)
    groups[k].append(microstate)
  return groups

