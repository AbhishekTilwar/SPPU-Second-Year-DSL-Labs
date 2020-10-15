#Name:Abhishek Tilwar
#Roll No:2101001
#Class: SE-A(Computer)
#Prn:72031575B
#DSL  Assignment-4

global a
a=list()
n=int(input("Enter the number of students in club: "))
for i in range(0,n):
    b=input("Enter student name: ")
    a.append(b)
a.sort()



def ternarySearch(l, r, key, a): 
    while r >= l: 
          
        mid1 = l + (r-l) // 3
        mid2 = r - (r-l) // 3
        if key == mid1: 
            return mid1 
        if key == mid2: 
            return mid2
        if key < mid1: 
            r = mid1 - 1
        elif key > mid2: 
            l = mid2 + 1
        else:  
            l = mid1 + 1
            r = mid2 - 1
    return -1

choice='random'
def line():
    print('---------------------------')

def show_menu():
    line()
    print('MENU')
    line()
    print('1. Linear Search')
    print('2. Binary Search')
    print('3. Ternary Search')
    print('4. Exit')
    line()
    choice = input('Enter your choice: ')
    return choice

def linear_search(a,x):
    for i in range(len(a)): 
  
        if i == x: 
            return i 
  
    return -1
    

def binary_search(a, low, high, x):

    if high >= low:
        mid = (high + low) // 2
  
        if mid == x: 
            return mid
        elif mid > x: 
            return binary_search(a, low, mid - 1, x) 
  
        else: 
            return binary_search(a, mid + 1, high, x) 
  
    else: 
        return -1

        
while choice != '4':
    choice = show_menu()
    if choice=='1':
        x=int(input("Enter the student to be searched by member id: "))
        z=linear_search(a,x)
        if z != -1:
            print("The student",a[x],"is member of club with member id",str(z))
        else:
            print("Student is not member of club.")



    elif choice=='2':
        x=int(input("Enter the student to be searched by member id: "))
        res = binary_search(a, 0, len(a)-1, x)
        if res != -1:
            print("The student",a[x],"is member of club with member id",str(res))

        else:
            print("Student is not member of club.")
            
    elif choice=='3':
        l=0
        r=len(a)
        key=int(input("Enter the student to be searched by member id: "))
        p = ternarySearch(l, r, key, a)
        if p != -1:
            print("The student",a[key],"is member of club with member id",str(p))
        else:
            print("Student is not member of club.")
    elif choice=='4':
        print("Goodbye")
    else:
        print("Incorrect choice")
  
'''
Output:-

Enter the number of students in club: 5
Enter student name: abhishek
Enter student name: yash
Enter student name: rahul
Enter student name: raj
Enter student name: omkar
---------------------------
MENU
---------------------------
1. Linear Search
2. Binary Search
3. Ternary Search
4. Exit
---------------------------
Enter your choice: 1
Enter the student to be searched by member id: 0
The student abhishek is member of club with member id 2
---------------------------
MENU
---------------------------
1. Linear Search
2. Binary Search
3. Ternary Search
4. Exit
---------------------------
Enter your choice: 3
Enter the student to be searched by member id: 4
The student yash is member of club with member id 4
---------------------------
MENU
---------------------------
1. Linear Search
2. Binary Search
3. Ternary Search
4. Exit
---------------------------
Enter your choice: 2
Enter the student to be searched by member id: 3
The student raj is member of club with member id 3
---------------------------
MENU
---------------------------
1. Linear Search
2. Binary Search
3. Ternary Search
4. Exit
---------------------------
Enter your choice: 4
Goodbye
'''
