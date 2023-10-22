## Programming Challenge: Efficiently Check for Immutable Common Elements
You are working on a software project that involves handling large datasets of product IDs. Due to the nature of the project, you frequently need to check for common product IDs between datasets. However, these datasets can get large, and your checks need to be both memory-efficient and fast.

For this challenge:

Implement a function named find_common_elements that takes in two lists, list1 and list2, representing two datasets of product IDs.

The function should return a frozenset containing the common product IDs found in both lists.

To demonstrate the immutability property of frozensets, ensure that once the common elements are found, they cannot be modified.

Constraints:

You should NOT use Python's inbuilt intersection method for sets.
Both input lists can have a length of up to 
10^5.
Product IDs are alphanumeric and can be up to 10 characters long.
Example:

```python
list1 = ["prod123", "prod567", "prod890"]
list2 = ["prod567", "prod891", "prod654"]
result = find_common_elements(list1, list2)
print(result)
```
Expected Output:

```python
frozenset({'prod567'})
```
Note: Use frozensets to solve this problem due to their immutability and set properties. This mirrors real-world scenarios where data consistency and prevention of unintended mutations are crucial, especially in large-scale data operations.