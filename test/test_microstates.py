import pytest
from src.microstates import(generate_microstates,count_heads,group_by_heads)

""" First we check the functions for N=3 because is quicker"""
def test_generate_microstates():
  result=generate_microstates(3)

  assert len(result)==8
  assert "TTT" in result
  assert "HHH" in result

def test_generate_microstates_invalid_N():
  with pytest.raises(ValueError):
    generate_microstates(0)

def test_count_heads():
  assert count_heads("HTH")==2
  assert count_heads("HHH")==3
  assert count_heads("TTT")==0

def test_count_heads_invalid_microstate():
  with pytest.raises(ValueError):
    count_heads("THA")
    
def test_group_by_heads():
  microstates=generate_microstates(3)
  groups=group_by_heads(microstates)

  assert len(groups[0])==1
  assert len(groups[1])==3
  assert len(groups[2])==3
  assert len(groups[3])==1

"""Now we check some of the functions for the N=7 cases, just to be safe"""
def test_generate_microstates_N7():
  result=generate_microstates(7)

  assert len(result)==128
  assert "TTTTTTT" in result
  assert "HHHHHHH" in result

def test_group_by_heads_N7():
  microstates=generate_microstates(7)
  groups=group_by_heads(microstates)

  assert len(groups[0])==1
  assert len(groups[1])==7
  assert len(groups[2])==21
  assert len(groups[3])==35
  assert len(groups[4])==35
  assert len(groups[5])==21
  assert len(groups[6])==7
  assert len(groups[7])==1


