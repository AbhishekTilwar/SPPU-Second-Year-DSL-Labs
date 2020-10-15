#Name:Abhishek Tilwar
#Roll No:2101001
#Class: SE-A(Computer)
#Prn:72031575B
#DSL  Assignment-3

def print_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print("\t", matrix[i][j], end=" ")
		print("\n")

def init_matrix(matrix, m, n):
	matrix = [[0 for j in range(0, n)] for i in range(0, m)]
	return matrix

def read_matrix():
	mat = []
	r = int(input("Enter number of rows in First Matrix: "))
	c = int(input("Enter number of columns in First Matrix :"))
	mat = init_matrix(mat, r, c) 
	for i in range(0, r):
 		for j in range(0, c):
 			mat[i][j] = int(input("Enter an element : "))
	return mat,r,c


def mat_add(m1, m2, res, m, n):
	for i in range(0, m):
 		for j in range(0, n):
 			res[i][j] = m1[i][j] + m2[i][j]
	return res

def mat_sub(m1, m2, res, m, n):
	for i in range(0, m):
 		for j in range(0, n):
 			res[i][j] = m1[i][j] - m2[i][j]
	return res

def mat_mul(m1, m2, res, r1, c1, c2):
	for i in range(0, r1):
		for k in range(0, c2):
			for j in range(0, c1):
 				res[i][k] += m1[i][j] * m2[j][k]
	return res

def trans_mat(m1, res, r1, c1):
	for i in range(0, r1):
 		for j in range(0, c1):
 			res[j][i] = m1[i][j]
	return res

matrix1 = []
matrix2 = []
res_matrix = []
print(" First Matrix : ")
matrix1, r1, c1 = read_matrix()
print(" Second Matrix : ")
matrix2, r2, c2 = read_matrix()
res_matrix = init_matrix(res_matrix, r1, c2) 

print(" matrix 1")
print_matrix(matrix1)
print(" matrix 2")
print_matrix(matrix2)
flag = 1

print("/************************************/ \n")
print(" 1. Addition of two matrices ")
print(" 2. Subtraction of two matrices ")
print(" 3. Multiplication of two matrices ")
print(" 4. Transpose of a matrix ")
choice = int(input("Enter Your Choice : "))
if choice == 1:
	if r1 == r2 and c1 == c2:
		print("resultant matrix after addition")
		res_matrix = mat_add(matrix1, matrix2, res_matrix, r1, c1)
		print_matrix(res_matrix)
	else:
		print("Addition can't be performed ")
elif choice == 2:
	if r1 == r2 and c1 == c2:
		print("resultant matrix after subtraction")
		res_matrix = mat_sub(matrix1, matrix2, res_matrix, r1, c1)
		print_matrix(res_matrix)
	else:
		print("Subtraction can't be performed ")
elif choice == 3:
	if c1 == r2:
		print("resultant matrix after Multiplication ")
		res_matrix = mat_mul(matrix1, matrix2, res_matrix, r1, c1, c2)
		print_matrix(res_matrix)
	else:
		print("Multiplication can't be performed ")
elif choice == 4:
	print("Transpose of First Matrix is ")
	res_matrix1 = []
	res_matrix1 = init_matrix(res_matrix1, c1, r1)
	res_matrix = trans_mat(matrix1, res_matrix1, r1, c1)
	print_matrix(res_matrix)
else:
	print(" Wrong choice ")
	flag = 0
'''
Output:-

 First Matrix :
Enter number of rows in First Matrix: 2
Enter number of columns in First Matrix :2
Enter an element : 1
Enter an element : 7
Enter an element : -3
Enter an element : 5
 Second Matrix :
Enter number of rows in First Matrix: 2
Enter number of columns in First Matrix :2
Enter an element : -1
Enter an element : -6
Enter an element : 2
Enter an element : 4
 matrix 1
         1       7

         -3      5

 matrix 2
         -1      -6

         2       4

/************************************/

 1. Addition of two matrices
 2. Subtraction of two matrices
 3. Multiplication of two matrices
 4. Transpose of a matrix
Enter Your Choice : 1
resultant matrix after addition
         0       1

         -1      9
 First Matrix : 
Enter number of rows in First Matrix: 2
Enter number of columns in First Matrix :2
Enter an element : 3
Enter an element : 1
Enter an element : 7
Enter an element : 11
 Second Matrix :
Enter number of rows in First Matrix: 2
Enter number of columns in First Matrix :2
Enter an element : 4
Enter an element : 2
Enter an element : 5
Enter an element : -1
 matrix 1
         3       1 

         7       11

 matrix 2
         4       2

         5       -1

/************************************/

 1. Addition of two matrices
 2. Subtraction of two matrices
 3. Multiplication of two matrices
 4. Transpose of a matrix
Enter Your Choice : 2
resultant matrix after subtraction
         -1      -1

         2       12
 First Matrix : 
Enter number of rows in First Matrix: 2
Enter number of columns in First Matrix :2
Enter an element : 7
Enter an element : 12
Enter an element : 9
Enter an element : 8
 Second Matrix :
Enter number of rows in First Matrix: 2
Enter number of columns in First Matrix :2
Enter an element : -5
Enter an element : -3
Enter an element : -1
Enter an element : -8
 matrix 1
         7       12

         9       8

 matrix 2
         -5      -3

         -1      -8

/************************************/

 1. Addition of two matrices
 2. Subtraction of two matrices
 3. Multiplication of two matrices
 4. Transpose of a matrix
Enter Your Choice : 3
resultant matrix after Multiplication
         -47     -117

         -53     -91
 First Matrix : 
Enter number of rows in First Matrix: 2
Enter number of columns in First Matrix :2
Enter an element : 1
Enter an element : 3
Enter an element : 5
Enter an element : 0
 Second Matrix :
Enter number of rows in First Matrix: 2
Enter number of columns in First Matrix :2
Enter an element : 8
Enter an element : 4
Enter an element : 0
Enter an element : 2
 matrix 1
         1       3

         5       0

 matrix 2
         8       4

         0       2

/************************************/

 1. Addition of two matrices
 2. Subtraction of two matrices
 3. Multiplication of two matrices
 4. Transpose of a matrix
Enter Your Choice : 4
Transpose of First Matrix is
         1       5

         3       0

'''	

