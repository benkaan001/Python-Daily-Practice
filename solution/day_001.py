from typing import Dict, Any, List, Optional
import re


def create_and_modify_profile(profile: Dict[str, Any]) -> Dict[str, Any]:
    """
    Modifies a user profile dictionary by adding, updating, and removing keys.
    This implementation modifies a copy to avoid side effects.
    """
    modified_profile = profile.copy()

    # Add a new key
    modified_profile["country"] = "USA"

    # Update an existing key
    modified_profile["city"] = "New York"

    # Remove a key, using .pop() for safety (doesn't error if key is missing)
    modified_profile.pop("email", None)

    return modified_profile


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
