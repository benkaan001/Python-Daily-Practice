import string
from typing import Any, Dict, List, Optional

# Note: 'Counter' is for the alternative solution in Exercise 2
# from collections import Counter


# --- Exercise 1: Dictionary Manipulation ---


def create_and_modify_profile(
    profile: Dict[str, Any], action: str, key: str, value: Optional[Any] = None
) -> Dict[str, Any]:
    """
    Solves Exercise 1 by manipulating a user profile dictionary.
    Returns a new, modified copy, leaving the original unchanged.
    """
    # INTERVIEW EXPLANATION (Method 1: Clear If/Elif):
    # "To ensure the original data is not changed, my first step is to create
    # a shallow copy of the input dictionary. This is a crucial best practice.
    # Then, I'll use a clear if/elif/else structure to handle the different
    # actions ('add', 'update', 'delete'). This approach is very readable
    # and makes the logic easy to follow."
    new_profile: Dict[str, Any] = profile.copy()

    if action == "add" and key not in new_profile:
        new_profile[key] = value
    elif action == "update" and key in new_profile:
        new_profile[key] = value
    elif action == "delete" and key in new_profile:
        del new_profile[key]

    return new_profile


# --- Exercise 2: Word Frequency ---


def count_word_frequency(sentence: str) -> Dict[str, int]:
    """
    Solves Exercise 2 by counting the frequency of words in a sentence.
    """
    # INTERVIEW EXPLANATION (Method 1: Manual Counting with .get()):
    # "My approach is to first process the input string to make it uniform.
    # This involves removing all punctuation and converting the string to
    # lowercase. Once cleaned, I'll split it into a list of words. Then,
    # I'll initialize an empty dictionary and loop through the words, using
    # the .get() method to increment the count for each word safely."
    word_counts: Dict[str, int] = {}

    # Create a translation table to remove all punctuation
    translator = str.maketrans("", "", string.punctuation)
    cleaned_sentence = sentence.translate(translator)

    words: List[str] = cleaned_sentence.lower().split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

    # ALTERNATIVE SOLUTION (Method 2: Using collections.Counter):
    # """
    # # For a more advanced and Pythonic solution, we can use the `Counter`
    # # class from Python's built-in `collections` module. It's specifically
    # # designed for this exact task. The process is similar: clean the string
    # # first, then pass the resulting list of words to the Counter object.
    # from collections import Counter
    # translator = str.maketrans('', '', string.punctuation)
    # cleaned_sentence = sentence.translate(translator)
    # words: List[str] = cleaned_sentence.lower().split()
    # return Counter(words)
    # """


# --- Exercise 3: Two Sum ---


def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Solves Exercise 3 by finding two numbers that add up to the target.
    """
    # INTERVIEW EXPLANATION (Method 1: O(n) with Hash Map):
    # "To solve this efficiently, I'll use a hash map (a Python dictionary)
    # to store the numbers we've seen and their indices. My approach has a
    # time complexity of O(n). I'll iterate through the list once. For each
    # number, I'll calculate its complement. If the complement is already in
    # my map, I've found the pair and can return their indices. If not, I'll
    # add the current number and its index to the map. If I finish the loop
    # without finding a pair, I'll return None as required."
    num_map: Dict[int, int] = {}  # To store number -> index
    for i, num in enumerate(nums):
        complement: int = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return None

    # ALTERNATIVE SOLUTION (Method 2: Brute-Force O(n^2)):
    # """
    # # A simpler, though less efficient, solution is the brute-force approach
    # # using nested loops. This has a time complexity of O(n^2). The outer
    # # loop picks a number, and the inner loop checks every other number to
    # # see if they sum to the target.
    # n: int = len(nums)
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    # return None
    # """
