def split_and_join(line):
    # write your code here
    list_new=line.split(" ")
    
    new_string="-".join(list_new)
    
    return new_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)