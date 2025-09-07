import pytest

# Import the functions to be tested from BOTH the practice and solution files
from practice.day_002 import (
    reverse_and_slice as practice_reverse,
    filter_products as practice_filter,
    rotate_list as practice_rotate,
)
from solution.day_002 import (
    reverse_and_slice as solution_reverse,
    filter_products as solution_filter,
    rotate_list as solution_rotate,
)

# --- Test Cases for Exercise 1: Reverse and Slice ---
reverse_params = [
    pytest.param(
        practice_reverse,
        marks=pytest.mark.xfail(reason="Practice file is intentionally empty"),
    ),
    pytest.param(solution_reverse),
]


@pytest.mark.parametrize("function_to_test", reverse_params)
def test_reverse_and_slice(function_to_test):
    assert function_to_test([1, 2, 3, 4, 5, 6]) == [6, 4, 2]
    assert function_to_test(["a", "b", "c", "d"]) == ["d", "b"]
    assert function_to_test([10]) == [10]
    assert function_to_test([]) == []


# --- Test Cases for Exercise 2: Filter Products ---
filter_params = [
    pytest.param(
        practice_filter,
        marks=pytest.mark.xfail(reason="Practice file is intentionally empty"),
    ),
    pytest.param(solution_filter),
]


@pytest.mark.parametrize("function_to_test", filter_params)
def test_filter_products(function_to_test):
    products_data = [
        {"name": "Laptop", "price": 1200, "in_stock": True},
        {"name": "Mouse", "price": 25, "in_stock": False},
        {"name": "Keyboard", "price": 75, "in_stock": True},
        {"name": "Monitor", "price": 300, "in_stock": True},
        {"name": "Webcam", "price": 100, "in_stock": False},
    ]
    assert function_to_test(products_data, 100) == ["Laptop", "Monitor"]
    assert function_to_test(products_data, 50) == [
        "Laptop",
        "Keyboard",
        "Monitor",
    ]
    assert function_to_test(products_data, 1500) == []


# --- Test Cases for Exercise 3: Rotate List ---
rotate_params = [
    pytest.param(
        practice_rotate,
        marks=pytest.mark.xfail(reason="Practice file is intentionally empty"),
    ),
    pytest.param(solution_rotate),
]


@pytest.mark.parametrize("function_to_test", rotate_params)
def test_rotate_list(function_to_test):
    # Basic case
    nums = [1, 2, 3, 4, 5, 6, 7]
    function_to_test(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    # Rotate by more than list length
    nums = [1, 2, 3]
    function_to_test(nums, 4)  # 4 % 3 = 1
    assert nums == [3, 1, 2]

    # Rotate by full length (should be unchanged)
    nums = ["a", "b", "c"]
    function_to_test(nums, 3)
    assert nums == ["a", "b", "c"]

    # Rotate empty list
    nums = []
    function_to_test(nums, 5)
    assert nums == []
