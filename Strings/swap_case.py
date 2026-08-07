def swap_case(s):
    list_format=list(s)
    
    length=len(list_format)
    
    for i in range(0,length):
        if list_format[i].isupper()==True:
            list_format[i]=list_format[i].lower()
        else:
            list_format[i]=list_format[i].upper()
    
    
    
    return "".join(list_format)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)