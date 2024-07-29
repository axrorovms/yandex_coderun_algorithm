from collections import Counter

length_of_list = int(input())
array = list(map(int, input().split()))

def count_unique_elements(arr: list):
    countered_array = Counter(arr)
    unique_elements = [i for i, j in countered_array.items() if j == 1]
    return len(unique_elements)

print(count_unique_elements(array))