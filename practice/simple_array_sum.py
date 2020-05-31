# Simple Array Sum
# Given an array of integers, find the sum of its elements.

def simpleArraySum(ar):
    """
    Returns the sum of the integers within `ar`

    Parameters
    ----------
    ar : list
        list of integers

    Returns
    -------
    int
        the sum of the list of integers
    """
    return sum(ar)


if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split(maxsplit=ar_count)))

    result = simpleArraySum(ar)

    print(result)
