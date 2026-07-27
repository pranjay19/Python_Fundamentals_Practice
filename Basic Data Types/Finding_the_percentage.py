if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    

avg_list=[]

for key,value in student_marks.items():
    if key==query_name:
        avg_list=value
        
avg=sum(avg_list)/len(avg_list)

print(f"{avg:.2f}")