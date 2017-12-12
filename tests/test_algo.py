import pytest
from allsortalgo.core import SortingAlgorithms


data = [6,8,3]
def test_bubblesort():
    assert SortingAlgorithms.BUBBLE(data) == [3,6,8]  


def test_insertion():
    assert SortingAlgorithms.INSERTION(data) == [3,6,8]


def test_merge():
    assert SortingAlgorithms.MERGE(data) == [3,6,8]


def test_listoflists():
	assert SortingAlgorithms.LISTOFLISTS([[5,8,9],[2,9]]) == [[2, 9], [5, 8, 9]]


def test_listoftuples():
    assert SortingAlgorithms.LISTOFTUPLES([(7,9,3), (6,9,1), (8,6,9)])	== [(6,9,1), (7,9,3), (8,6,9)]


def test_applysort():
	assert SortingAlgorithms.APPLYSORT([-5, -2, -6], lambda x: x * x)


def test_selectionsort():
	assert SortingAlgorithms.SELECTIONSORT(data) == [3,6,8]


def test_qucksort():
	n = len(data)
	assert SortingAlgorithms.QUICKSORT(data, 0, n - 1) == [3, 6, 8]


def test_heapsort():
	assert SortingAlgorithms.HEAPSORT(data) == [3, 6, 8]