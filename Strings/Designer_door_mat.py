# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read input from STDIN
row, column = map(int, input().split())

#first_half

for i in range(1,row,2):
    pattern=".|."*i
    print(pattern.center(column,"-"))

#center
print("WELCOME".center(column,"-"))


#second_half
for i in range(row-2, -1, -2):
    pattern = '.|.' * i
    print(pattern.center(column, '-'))