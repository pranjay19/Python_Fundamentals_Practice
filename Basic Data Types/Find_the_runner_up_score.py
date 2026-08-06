if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
updated_val=set(arr)
updated_list=sorted(list(updated_val))

print(updated_list[-2])