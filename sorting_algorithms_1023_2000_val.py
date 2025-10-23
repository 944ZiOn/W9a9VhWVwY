# 代码生成时间: 2025-10-23 20:00:14
import numpy as np

"""
Sorting Algorithms Module

This module provides a collection of sorting algorithms
implemented in Python using NumPy for performance.

Attributes:
    None

Methods:
    bubble_sort(arr): Bubble sort algorithm implementation.
    insertion_sort(arr): Insertion sort algorithm implementation.
    selection_sort(arr): Selection sort algorithm implementation.
"""


def bubble_sort(arr):
    """Bubble Sort Algorithm.
    
    Parameters:
    arr (numpy.ndarray): The array to be sorted.
    
    Returns:
    numpy.ndarray: The sorted array.
    
    Raises:
    TypeError: If the input is not a NumPy array.
    """
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a NumPy array.")
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def insertion_sort(arr):
    """Insertion Sort Algorithm.
    
    Parameters:
    arr (numpy.ndarray): The array to be sorted.
    
    Returns:
    numpy.ndarray: The sorted array.
    
    Raises:
    TypeError: If the input is not a NumPy array.
    """
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a NumPy array.")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    """Selection Sort Algorithm.
    
    Parameters:
    arr (numpy.ndarray): The array to be sorted.
    
    Returns:
    numpy.ndarray: The sorted array.
    
    Raises:
    TypeError: If the input is not a NumPy array.
    """
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a NumPy array.")
    
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage:
if __name__ == "__main__":
    arr = np.array([64, 34, 25, 12, 22, 11, 90])
    print("Original array: ", arr)
    print("Sorted array (Bubble Sort): ", bubble_sort(arr.copy()))  # Using copy to avoid modifying the original array
    print("Sorted array (Insertion Sort): ", insertion_sort(arr.copy()))
    print("Sorted array (Selection Sort): ", selection_sort(arr.copy()))