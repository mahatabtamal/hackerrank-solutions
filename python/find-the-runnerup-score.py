if __name__ == '__main__':
    n = int(input())
    array = map(int, input().split())
    new_set = list(set(num for num in array))
    new_set.sort()
    print(new_set[1])
    
    
