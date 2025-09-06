from typing import Dict, List, Optional
import re


def create_and_modify_profile(profile, action, key, value=None):
    """
    Exercise 1: Modify a user profile dictionary.
    - 'add': Add a new key-value pair.
    - 'update': Update an existing key.
    - 'delete': Remove a key.

    IMPORTANT: This function should be 'immutable'. It must return a new,
    modified copy of the dictionary and leave the original unchanged.
    """
    # Create a new copy to ensure the original is not modified.
    new_profile = profile.copy()

    if action == "add":
        if key not in new_profile:
            new_profile[key] = value
    elif action == "update":
        if key in new_profile:
            new_profile[key] = value
    elif action == "delete":
        if key in new_profile:
            del new_profile[key]

    # Return the modified copy, or the original copy if action was invalid
    return new_profile


def count_word_frequency(sentence: str) -> Dict[str, int]:
    """
    Counts the frequency of words in a sentence, case-insensitively,
    and ignoring punctuation.
    """
    if not sentence:
        return {}

    # Convert to lowercase
    normalized_sentence = sentence.lower()

    # Remove all characters that are not letters, numbers, or whitespace
    normalized_sentence = re.sub(r"[^\w\s]", "", normalized_sentence)

    # Split the sentence into words
    words = normalized_sentence.split()

    # Count the frequency of each word
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Finds two numbers in a list that sum up to a specific target and
    returns their indices. Returns None if no solution is found.
    This solution uses a hash map for O(n) time complexity.
    """
    num_map = {}  # To store number -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            # Found the pair
            return [num_map[complement], i]
        # Store the current number's index
        num_map[num] = i

    # If the loop completes, no solution was found
    return None


if __name__ == "__main__":
    print("This script is not intended to be run directly.")
