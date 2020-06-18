'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    if len(arr) > 0:
        maxi = max(arr)
        count = [0 for i in range(maxi + 1)]
        for i in range(len(arr)):
            val = arr[i]
            count[val] += 1
        for i in range(len(count)):
            if count[i] == 1:
                return i


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 9, 20, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
