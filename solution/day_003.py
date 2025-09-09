from typing import List, Set, Tuple, Any

# --- Exercise 1: Finding Unique Elements ---


def find_unique_elements(data: List[Any]) -> List[Any]:
    """
    Solves Exercise 1 by taking a list of items and returning a new list
    containing only the unique elements from the original list, while
    preserving the original order.
    """
    # INTERVIEW EXPLANATION (Method 1: Using a Set for Tracking):
    # "To solve this problem while preserving order, I'll use a combination of
    # a list for the results and a set for tracking seen items. This approach
    # has a time complexity of O(n) because I iterate through the list once,
    # and each check in the `seen` set is an O(1) operation.
    # I'll initialize an empty list `unique_items` and an empty set `seen`.
    # Then, I'll loop through the input list. For each item, I check if it's
    # already in the `seen` set. If it's not, I add it to both `unique_items`
    # and `seen`. If it is, I do nothing. This ensures each unique item is
    # added only the first time it's encountered."
    seen: Set[Any] = set()
    unique_items: List[Any] = []
    for item in data:
        if item not in seen:
            unique_items.append(item)
            seen.add(item)
    return unique_items

    # ALTERNATIVE SOLUTION (Method 2: Python 3.7+ Dictionary Keys):
    # """
    # # For a more modern and concise solution that works in Python 3.7+,
    # # we can leverage the fact that standard dictionaries now preserve
    # # insertion order. We can convert the list into a dictionary using
    # # `dict.fromkeys()`, which automatically handles uniqueness by using
    # # the list items as keys. Then, we can simply convert the dictionary's
    # # keys back into a list. The result is a unique, ordered list.
    # return list(dict.fromkeys(data))
    # """


# --- Exercise 2: Comparing Sets of Skills ---


def get_common_and_different_skills(
    skills1: List[str], skills2: List[str]
) -> Tuple[Set[str], Set[str]]:
    """
    Solves Exercise 2 by taking two lists of skills and returning a tuple
    containing two sets: common skills and skills unique to the first list.
    """
    # INTERVIEW EXPLANATION (Method 1: Using Set Operations):
    # "The most efficient and readable way to solve this is to first convert
    # both lists into sets. This immediately handles any duplicates within
    # each list and prepares the data for high-speed set operations.
    # To find the common skills, I'll use the intersection operator (`&`).
    # To find the skills unique to the first candidate, I'll use the
    # difference operator (`-`). These operations are highly optimized, making
    # the code both performant and expressive."
    set1 = set(skills1)
    set2 = set(skills2)

    common_skills: Set[str] = set1 & set2  # Intersection
    unique_to_first: Set[str] = set1 - set2  # Difference

    return (common_skills, unique_to_first)


# --- Exercise 3: Detecting Duplicates ---


def has_duplicate_characters(s: str) -> bool:
    """
    Solves Exercise 3 by taking a string and returning True if it contains
    any duplicate characters, and False otherwise.
    """
    # INTERVIEW EXPLANATION (Method 1: Comparing Lengths):
    # "My approach is to leverage a set's core property of storing only unique
    # elements. I can convert the input string directly into a set of its
    # characters. If there are any duplicate characters in the original
    # string, the resulting set will be smaller in length than the string.
    # Therefore, I can simply compare the length of the set to the length
    # of the original string. If they are not equal, it means duplicates
    # were present, and I can return True."
    return len(set(s)) != len(s)

    # ALTERNATIVE SOLUTION (Method 2: Iterative with a Set):
    # """
    # # Another way to solve this, which can be more memory-efficient for
    # # very long strings with an early duplicate, is to iterate through the
    # # string character by character. I'll use a `seen` set to keep track of
    # # the characters I've encountered. For each character, I check if it's
    # # already in the `seen` set. If it is, I've found a duplicate and can
    # # immediately return `True`. If not, I add the character to the set.
    # # If I get through the whole loop without finding duplicates, I return
    # # `False`. This approach has the same O(n) time complexity but can
    # # short-circuit and return early.
    # seen: Set[str] = set()
    # for char in s:
    #     if char in seen:
    #         return True
    #     seen.add(char)
    # return False
    # """
