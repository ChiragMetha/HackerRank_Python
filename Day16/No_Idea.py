"""https://www.hackerrank.com/challenges/no-idea/problem"""

"""No Idea
"""
if __name__ == "__main__":
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    elements_arr = list(map(int, input().strip().split(' ')))
    
    A = set(map(int, input().strip().split(' ')))
    B = set(map(int, input().strip().split(' ')))
    
    for i in elements_arr:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    print(happiness)