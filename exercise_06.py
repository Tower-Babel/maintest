#exercise_06
matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
r = int(input("enter a row num from 1 to 5: "))
c = int(input("enter a col num from 1 to 5: "))
matrix[r-1][c-1] = 1
for i in matrix:
    print(i)