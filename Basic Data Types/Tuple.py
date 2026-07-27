if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    tuple_val=tuple(integer_list)

    print hash(tuple_val)

#Note this is working only in python 2 version as hashvalue are coming different in python 3. 