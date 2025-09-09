import pytest

# Import the user's practice functions and the official solution functions
from practice.day_003 import (
    find_unique_elements as practice_unique,
    get_common_and_different_skills as practice_skills,
    has_duplicate_characters as practice_duplicates,
)
from solution.day_003 import (
    find_unique_elements as solution_unique,
    get_common_and_different_skills as solution_skills,
    has_duplicate_characters as solution_duplicates,
)

# --- Parametrization ---
unique_params = [
    pytest.param(
        practice_unique,
        marks=pytest.mark.xfail(reason="Practice code not yet implemented"),
    ),
    pytest.param(solution_unique),
]

skills_params = [
    pytest.param(
        practice_skills,
        marks=pytest.mark.xfail(reason="Practice code not yet implemented"),
    ),
    pytest.param(solution_skills),
]

duplicates_params = [
    pytest.param(
        practice_duplicates,
        marks=pytest.mark.xfail(reason="Practice code not yet implemented"),
    ),
    pytest.param(solution_duplicates),
]


# --- Tests for Exercise 1: Finding Unique Elements ---


@pytest.mark.parametrize("function_to_test", unique_params)
def test_find_unique_elements(function_to_test):
    # Basic case with numbers and strings
    assert function_to_test([1, 2, "a", 3, "b", 2, "a", 1]) == [
        1,
        2,
        "a",
        3,
        "b",
    ]
    # Case with no duplicates
    assert function_to_test([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    # Case with all same elements
    assert function_to_test(["x", "x", "x"]) == ["x"]
    # Case with empty list
    assert function_to_test([]) == []
    # Case with mixed types and order
    assert function_to_test([None, 1, "a", None, "a", 1]) == [None, 1, "a"]


# --- Tests for Exercise 2: Comparing Sets of Skills ---


@pytest.mark.parametrize("function_to_test", skills_params)
def test_get_common_and_different_skills(function_to_test):
    c1 = ["Python", "SQL", "Docker", "Git"]
    c2 = ["Java", "SQL", "Cloud", "Python"]
    common, unique = function_to_test(c1, c2)
    assert isinstance(common, set)
    assert isinstance(unique, set)
    assert common == {"Python", "SQL"}
    assert unique == {"Docker", "Git"}

    # Case with no common skills
    c3 = ["Go", "Rust"]
    common, unique = function_to_test(c1, c3)
    assert common == set()
    assert unique == {"Python", "SQL", "Docker", "Git"}

    # Case with identical skills
    common, unique = function_to_test(c1, c1)
    assert common == {"Python", "SQL", "Docker", "Git"}
    assert unique == set()

    # Case with empty lists
    common, unique = function_to_test([], [])
    assert common == set()
    assert unique == set()


# --- Tests for Exercise 3: Detecting Duplicates ---


@pytest.mark.parametrize("function_to_test", duplicates_params)
def test_has_duplicate_characters(function_to_test):
    assert function_to_test("hello") is True
    assert function_to_test("world") is False
    assert function_to_test("Python") is False
    # Case sensitive
    assert function_to_test("Apple") is True
    assert function_to_test("apple") is True
    # Empty string
    assert function_to_test("") is False
    # String with space
    assert (
        function_to_test("the quick brown fox") is True
    )  # space is duplicated
