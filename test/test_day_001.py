import pytest

# Import the functions to be tested from BOTH the practice and solution files
from practice.day_001 import (
    create_and_modify_profile as practice_create,
    count_word_frequency as practice_count,
    two_sum as practice_two_sum,
)
from solution.day_001 import (
    create_and_modify_profile as solution_create,
    count_word_frequency as solution_count,
    two_sum as solution_two_sum,
)

# Use pytest.mark.parametrize to create a list of functions to test
# This allows us to run the same tests on both the practice and solution code
functions_to_test = [practice_create, solution_create]


@pytest.mark.parametrize("function_to_test", functions_to_test)
def test_create_and_modify_profile(function_to_test):
    """
    Tests the basic creation, update, and deletion of profile entries.
    """
    profile = {"name": "Ben", "email": "ben@example.com"}

    # Test adding a new key
    modified_profile = function_to_test(profile, "add", "country", "Thailand")
    assert "country" in modified_profile
    assert modified_profile["country"] == "Thailand"

    # Test updating an existing key
    modified_profile = function_to_test(profile, "update", "name", "Benjamin")
    assert modified_profile["name"] == "Benjamin"

    # Test deleting a key
    modified_profile = function_to_test(profile, "delete", "email")
    assert "email" not in modified_profile

    # Test invalid action
    modified_profile = function_to_test(
        profile, "invalid_action", "key", "value"
    )
    assert modified_profile == profile  # Profile should be unchanged


# Parametrize for the word frequency counter function
functions_to_test_count = [practice_count, solution_count]


@pytest.mark.parametrize("function_to_test", functions_to_test_count)
def test_count_word_frequency(function_to_test):
    """
    Tests the word frequency counting logic.
    """
    sentence = "Hello world hello"
    expected = {"hello": 2, "world": 1}
    assert function_to_test(sentence) == expected

    sentence_with_case = "The quick brown fox jumps over the lazy dog Dog."
    expected_with_case = {
        "the": 2,
        "quick": 1,
        "brown": 1,
        "fox": 1,
        "jumps": 1,
        "over": 1,
        "lazy": 1,
        "dog": 2,
    }
    assert function_to_test(sentence_with_case) == expected_with_case

    empty_sentence = ""
    assert function_to_test(empty_sentence) == {}


# Parametrize for the two_sum function
functions_to_test_two_sum = [practice_two_sum, solution_two_sum]


@pytest.mark.parametrize("function_to_test", functions_to_test_two_sum)
def test_two_sum(function_to_test):
    """
    Tests the two_sum logic with various scenarios.
    """
    # Basic case
    assert sorted(function_to_test([2, 7, 11, 15], 9)) == [0, 1]

    # Case with negative numbers
    assert sorted(function_to_test([-1, 5, 10, 11], 9)) == [0, 2]

    # Case where two numbers are the same
    assert sorted(function_to_test([3, 3], 6)) == [0, 1]

    # No solution case
    assert function_to_test([1, 2, 3], 7) is None

    # Larger list
    assert sorted(function_to_test([10, 20, 30, 40, 50], 90)) == [3, 4]
