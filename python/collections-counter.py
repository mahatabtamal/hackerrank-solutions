from collections import Counter

num_of_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))
customers = int(input())
earnings = 0

for i in range(customers):
    size, price = list(map(int, input().split()))
    if shoe_sizes[size] != 0:
        earnings += price
        shoe_sizes[size] -= 1
print(earnings)
