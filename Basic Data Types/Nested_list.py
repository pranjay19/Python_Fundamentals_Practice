if __name__ == '__main__':
    
    student_list=[]
        
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        
        student_list.append([name,score])
        
    scores_list=[]
    
    for i in range(len(student_list)):
        scores_list.append(student_list[i][1])
        
    scores_list=sorted(list(set(scores_list)))
    
    second_lowest_score=scores_list[1]
    
    final_name_list=[]
    
    for i in range(len(student_list)):
        if student_list[i][1]==second_lowest_score:
            final_name_list.append(student_list[i][0])
        else:
            continue
    final_name_list=sorted(final_name_list)
    
     
    
    for i in range(len(final_name_list)):
        print(final_name_list[i])
        
        
        
        