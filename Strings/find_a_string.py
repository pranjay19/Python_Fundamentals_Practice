def count_substring(string, sub_string):
    
    sub_len=len(sub_string)
    count=0
    
    for i in range(len(string)-sub_len+1):
        if string[i]==sub_string[0]:
            val=0
            for j in range(sub_len):
                if string[i+j]==sub_string[j]:
                    val+=1
                else: 
                    continue
            if val==sub_len:
                count+=1
            else:
                continue 
        else:
            continue
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)