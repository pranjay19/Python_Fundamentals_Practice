if __name__ == '__main__':
    N = int(input())
List_final=[]  
for i in range(N):
    list_temp=input().split()
    for i in range(len(list_temp)):
        if list_temp[i]=="insert":
            List_final.insert(int(list_temp[i+1]),int(list_temp[i+2]))
            break
        elif list_temp[i]=="print":
            print(List_final)
            break
        elif list_temp[i]=="remove":
            List_final.remove(int(list_temp[i+1]))
            break
        elif list_temp[i]=="append":
            List_final.append(int(list_temp[i+1]))
            break
        elif list_temp[i]=="sort":
            List_final.sort()
            break
        elif list_temp[i]=="pop":
            List_final.pop()
            break
        elif list_temp[i]=="reverse":
            List_final.reverse()
            break
        else:
            break
        
        
            
    