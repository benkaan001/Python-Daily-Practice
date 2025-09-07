from typing import Any, Dict, List

# --- Exercise 1: Advanced Slicing ---


def reverse_and_slice(data: List[Any]) -> List[Any]:
    """
    Solves Exercise 1 by returning every other element in reverse order.
    """
    # INTERVIEW EXPLANATION (Method 1: Direct Slicing):
    # "For this problem, Python's extended slicing is both the most efficient
    # and the most readable solution. The slice `[::-2]` elegantly expresses
    # the logic: start from the end, step backwards by two. It's a clear
    # demonstration of Python proficiency."
    return data[::-2]

    # ALTERNATIVE SOLUTION (Method 2: Multi-Step):
    # """
    # # For clarity, we could also solve this step-by-step. First, reverse
    # # the entire list. Then, loop through the reversed list and add every
    # # other element to a new results list.
    # reversed_list: List[Any] = data[::-1]
    # result: List[Any] = []
    # for i, item in enumerate(reversed_list):
    #     if i % 2 == 0:
    #         result.append(item)
    # return result
    # """


# --- Exercise 2: List Comprehensions ---


def filter_products(
    products: List[Dict[str, Any]], min_price: int
) -> List[str]:
    """
    Solves Exercise 2 by filtering a list of product dictionaries.
    """
    # INTERVIEW EXPLANATION (Method 1: For-Loop):
    # "To start, I'll use a simple and clear for-loop. This approach is very
    # transparent and easy to talk through. I'll initialize an empty list,
    # iterate through each product, check if it meets both conditions, and if
    # so, append its name to the results list."
    filtered_names: List[str] = []
    for product in products:
        if product["in_stock"] and product["price"] > min_price:
            filtered_names.append(product["name"])
    return filtered_names

    # ALTERNATIVE SOLUTION (Method 2: List Comprehension):
    # """
    # # For a more concise and 'Pythonic' implementation, we can refactor this
    # # using a list comprehension. It achieves the exact same result in a
    # # single, expressive line of code.
    # return [
    #     product["name"]
    #     for product in products
    #     if product["in_stock"] and product["price"] > min_price
    # ]
    # """


# --- Exercise 3: In-Place Modification ---


def rotate_list(nums: List[int], k: int) -> None:
    """
    Solves Exercise 3 by rotating a list to the right by k steps in-place.
    """
    # INTERVIEW EXPLANATION (Method 1: O(n) space):
    # "My first approach uses an auxiliary list, which is straightforward.
    # The time and space complexity will be O(n). I'll create a new list,
    # place each element in its new rotated position, and finally, use a
    # slice assignment `nums[:]` to copy the contents back into the
    # original list to modify it in-place."
    if not nums:
        return

    n: int = len(nums)
    k %= n

    rotated_nums: List[int] = [0] * n
    for i in range(n):
        rotated_nums[(i + k) % n] = nums[i]

    nums[:] = rotated_nums

    # ALTERNATIVE SOLUTION (Method 2: O(1) space):
    # """
    # # For a more optimal solution, we can achieve this with O(1) space
    # # complexity by using Python's slice assignment. We construct the
    # # rotated list by taking the last 'k' elements and placing them before
    # # the first 'n-k' elements, then replace the list's contents in-place.
    # if not nums:
    #     return
    # n: int = len(nums)
    # k %= n
    # nums[:] = nums[n - k:] + nums[: n - k]
    # """
