import pytest
from allsortalgo.core import SortingAlgorithms


data = [6,8,3]
def test_bubblesort():
    assert SortingAlgorithms.BUBBLE(data) == [3,6,8]  

def test_insertion():
    assert SortingAlgorithms.INSERTION(data) == [3,6,8]

def test_merge():
    assert SortingAlgorithms.MERGE(data) == [3,6,8]

# def test_quick():
#     assert SortingAlgorithms.QUICK(data) == [3,6,8] 

# def test_             
