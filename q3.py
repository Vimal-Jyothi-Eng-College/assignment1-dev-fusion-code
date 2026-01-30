"""c) Write a Python program to implement matrix multiplication."""

r1=int(input("Enter number of Rows of First Matrix: "))
c1=int(input("Enter number of Columns of First Matrix: "))
r2=int(input("Enter number of Rows of Second Matrix: "))
c2=int(input("Enter number of Columns of Second Matrix: "))

if c1!=r2:
    print("Matrix cannot be Multiplied!!!")
else:
    print("Enter Elements of First Matrix: ")
    A=[]
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(int(input(f"A[{i}][{j}]: ")))
        A.append(row)

    print("Enter Elements of Second Matrix: ")
    B=[]
    for i in range(r2):
        row=[]
        for j in range(c2):
            row.append(int(input(f"B[{i}][{j}]: ")))
        B.append(row)

    result=[[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j]+=A[i][k]*B[k][j]

    print("Resultant Matrix: ")
    for row in result:
        print(row)