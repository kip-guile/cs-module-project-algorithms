'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    pointerA = 0
    pointerB = pointerA + k
    new = []

    while pointerB <= len(nums):
        sliced = nums[pointerA:pointerB]
        maxNum = max(sliced)
        new.append(maxNum)
        pointerA += 1
        pointerB += 1

    return new


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
