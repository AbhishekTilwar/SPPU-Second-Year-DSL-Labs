#Name:Abhishek Tilwar
#Roll No:2101001
#Class: SE-A(Computer)
#Prn:72031575B
#DSL  Assignment-5

global a
a=list()
n=int(input("Enter the number of students: "))
for i in range(0,n):
    b=float(input("Enter percentage of student: "))
    a.append(b)
print(a)

choice='random'
def line():
    print('---------------------------')

def show_menu():
    line()
    print('MENU')
    line()
    print('1. Selection sort')
    print('2. Bubble sort')
    print('3. Top five percentage of student.')
    print('4. Exit')
    line()
    choice = input('Enter your choice: ')
    return choice 
 
def bubbleSort(a): 
    n = len(a) 
    for i in range(n):  
        for j in range(0, n-i-1): 
            if a[j] > a[j+1] : 
                a[j], a[j+1] = a[j+1], a[j]

def selectionsort(a):
    for i in range(len(a)):
            min_idx = i
            for j in range(i+1, len(a)):
                if a[min_idx] > a[j]:
                    min_idx = j 
            a[i], a[min_idx] = a[min_idx], a[i]



while choice != '4':
    choice = show_menu()
    if choice=='1':
        selectionsort(a)
        print ("Sorted array is")
        for i in range(len(a)):
            print("%0.2f" %a[i])        
    
    elif choice=='2':
        bubbleSort(a)
        print ("Sorted array is:")
        for i in range(len(a)):
            print ("%0.2f" %a[i])

    elif choice=='3':
        n = len(a)
        for i in range(n):
            for j in range(0, n-i-1):
                if a[j] < a[j+1] :
                    a[j], a[j+1] = a[j+1], a[j]
        print("The top five percentages are: ")
        for i in range(0,5):
            print ("%0.2f" %a[i])
    elif choice=='4':
        print("Goodbye")
    else:
        print("Incorrect choice")

'''
Output:-

Enter the number of students: 10
Enter percentage of student: 34.5
Enter percentage of student: 78.96
Enter percentage of student: 53.34
Enter percentage of student: 89.23
Enter percentage of student: 95.42
Enter percentage of student: 81.43
Enter percentage of student: 77.2
Enter percentage of student: 73.4
Enter percentage of student: 64.21
Enter percentage of student: 93.21
[34.5, 78.96, 53.34, 89.23, 95.42, 81.43, 77.2, 73.4, 64.21, 93.21]
---------------------------
MENU
---------------------------
1. Selection sort
2. Bubble sort
3. Top five percentage of student.
4. Exit
---------------------------
Enter your choice: 1
Sorted array is
34.50
53.34
64.21
73.40
77.20
78.96
81.43
89.23
93.21
95.42
---------------------------
MENU
---------------------------
1. Selection sort
2. Bubble sort
3. Top five percentage of student.
4. Exit
---------------------------
Enter your choice: 2
Sorted array is:
34.50
53.34
64.21
73.40
77.20
78.96
81.43
89.23
93.21
95.42
---------------------------
MENU
---------------------------
1. Selection sort
2. Bubble sort
3. Top five percentage of student.
4. Exit
---------------------------
Enter your choice: 3
The top five percentages are: 
95.42
93.21
89.23
81.43
78.96
---------------------------
MENU
---------------------------
1. Selection sort
2. Bubble sort
3. Top five percentage of student.
4. Exit
---------------------------
Enter your choice: 4
Goodbye

'''
