"""https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem"""

"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
print runner up socre 
input = 5
imput = 2 3 6 6 5"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = set(arr)
    arr2 = sorted[arr1]
    print(arr2[-2])