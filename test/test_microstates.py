import pytest
from src.microstates import(generate_microstates,count_heads,group_by_heads)

def test_generate_microstates():
  result=generate_microstates(3)

  assert len(result)==8
  assert "000" in result
  assert "111" in result

def test_generate_microstates_invalid_N():
  with pytest.raises(ValueError):
    generate_microstates(0)

def test_count_heads():
  assert count_heads("101")==2
  assert count_Heads("111")==3
  assert count_heads("000")==0

def test_count_heads_invalid_microstate():
  with pytest.raises(ValueError):
    count_heads("10A")
    
def test_group_by_heads():
  microstates=generate_microstates(3)
  groups=gropu_by_heads(microstates)

  assert len(gropus[0])==1
  assert len(gropus[1])==3
  assert len(gropus[2])==3
  assert len(gropus[3])==1



