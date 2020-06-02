"""Multiples of 3 and 5"""

# PROBLEM 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_of_3_and_5(n = 1000):
    return sum([i for i in range(1,n) if (i%3 == 0) or (i%5 == 0)])

if __name__ == "__main__":
    print(multiples_of_3_and_5(1000))
    
