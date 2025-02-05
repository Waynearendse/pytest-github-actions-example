# Import the pytest module for testing
import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from src.area import calculate_area_square

# Define a test function to test the calculate_area_square function with valid inputs
def test_calculate_area_square():
    # Check if the area of a square with length 2 is equal to 4
    assert calculate_area_square(2) == 4
    # Check if the area of a square with length 2.5 is equal to 6.25
    assert calculate_area_square(2.5) == 6.25

# Define a test function to test the calculate_area_square function with a negative input
def test_calculate_area_square_negative():
    # Check if the function raises a TypeError when called with a negative length
    with pytest.raises(TypeError):
        calculate_area_square(-2)

# Define a test function to test the calculate_area_square function with a string input
def test_calculate_area_square_string():
    # Check if the function raises a TypeError when called with a string length
    with pytest.raises(TypeError):
        calculate_area_square("2")

# Define a test function to test the calculate_area_square function with a list input
def test_calculate_area_square_list():
    # Check if the function raises a TypeError when called with a list as length
    with pytest.raises(TypeError):
        calculate_area_square([2])
