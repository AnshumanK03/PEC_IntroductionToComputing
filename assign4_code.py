#Assignment 3

#Question 1
print('Input the number of rings for the tower of hanoi')
rings=int(input())

   
print("The program assumes that the initial tower (where the discs are initially kept) is 1st one and the final tower (where the discs will finally be moved) is 3rd")

i=rings
discs_in_the_given_tower=dict()
discs_in_the_given_tower['1']=[]
discs_in_the_given_tower['2']=[]
discs_in_the_given_tower['3']=[]

while(i>0):
 discs_in_the_given_tower['1'].append((i))
 i=i-1

print('1:', end=" ")
print(discs_in_the_given_tower['1'])
print('2:', end=" ")
print(discs_in_the_given_tower['2'])
print('3:', end=" ")
print(discs_in_the_given_tower['3'])


def hanoi(n,source,spare,sink):

 if((n==1)):
  discs_in_the_given_tower[source].remove(1)
  discs_in_the_given_tower[sink].append(1)
  print('1:', end=" ")
  print(discs_in_the_given_tower['1'])
  print('2:', end=" ")
  print(discs_in_the_given_tower['2'])
  print('3:', end=" ")
  print(discs_in_the_given_tower['3'])
 
 if(n>1):
  hanoi((n-1),source,sink,spare)
  discs_in_the_given_tower[source].remove(n)
  discs_in_the_given_tower[sink].append(n)
  print('1:', end=" ")
  print(discs_in_the_given_tower['1'])
  print('2:', end=" ")
  print(discs_in_the_given_tower['2'])
  print('3:', end=" ")
  print(discs_in_the_given_tower['3'])
  hanoi((n-1),spare,source,sink)
  


  


hanoi(rings,'1','2','3')
print('1:', end=" ")
print(discs_in_the_given_tower['1'])
print('2:', end=" ")
print(discs_in_the_given_tower['2'])
print('3:', end=" ")
print(discs_in_the_given_tower['3'])
 
 
 
 
  
#Question 2
print('Input the number of rows for which the pascal triangle is to be printed')
rows=int(input())
m=1
row_elements=1
list_containing_row_elements=[1,1]
list_of_rows=[[1,]]
list_of_rows.append(list_containing_row_elements)
def row():
 list_containing_row_elements=[1,]
 n=0
 a=1
 list_of_previous_row_elements=list_of_rows[m]
 while(n<(len(list_of_previous_row_elements)-1)):
  list_containing_row_elements.append((list_of_previous_row_elements[a-1]+list_of_previous_row_elements[a]))
  n=n+1
  a=a+1
 list_containing_row_elements.append(1)
 list_of_rows.append(list_containing_row_elements)
while(m<(rows-1)):
 row()
 m=m+1

j=0
m=rows-1
for k in list_of_rows:
 string_containing_row_elements=""
 for l in k:
  string_containing_row_elements=string_containing_row_elements+str(l)+"   "
 print(("  "*m)+string_containing_row_elements)
 m=m-1
  
   
 

  
  
#Question 3
integer1=int(input("Enter Integer 1 "))
integer2=int(input("Enter Integer 2 "))
def quotient(a,b):
 return (int(a/b))
def remainder(a,b):
 return a%b
if ((not(integer1==0))and(not(integer2==0))):
 print("The quotient of the first and second integer is ",quotient(integer1,integer2))
 print("The remainder of first and second integer is ",remainder(integer1,integer2))
else:
 print("One of the input integer is 0")
list1=[]
addlist=[4,5,6]
list1.append(quotient(integer1,integer2))
list1.append(remainder(integer1,integer2))
for i in addlist:
 list1.append(i)
list1.sort()
print("The elements greater than four in the resulting list are ",list1[(list1.index(4)+1):])
set_for_the_result=set(list1)
print("The set for the resulting list is",set_for_the_result)
print("The maximum value from the set is",list1[len(list1)-1])
print("The immutable set is",frozenset(set_for_the_result))
print("The hash value for the maximum value is",hash(list1[len(list1)-1]))





#Question 4
list_of_names=[]
list_of_roll_numbers=[]
prompt='y'
Dictionary_of_students={}
students=[1,]

class Student:

 def _init_(self):
  
  self.name=""
  self.roll_number=0
  
 def _del_(self):
  print('Destructor called')

i=0
while(prompt=='y'):
 a=Student()
 print('Please enter the name of student')
 a.name=input()
 list_of_names.append(a.name)
 print('Please enter the roll number of the student')
 a.roll_number=int(input())
 list_of_roll_numbers.append(a.roll_number)
 print("Hit 'y' to continue adding more names and any other letter to exit")
 prompt=input()
 
i=0
corresponding_dictionary=dict()
while(i<(len(list_of_names))):
  corresponding_dictionary[list_of_names[i]]=list_of_roll_numbers[i]
  i=i+1
print('The data of the students stored in a dictionary is as follows')
print(corresponding_dictionary)


a._del_()





#Question 5
class Employee:

 def _init_(self):
  self.name=""
  self.salary=0
  
 def _del_(self):
  print('Record of the called employee deleted')

employee1=Employee()
employee2=Employee()
employee3=Employee()
employee1.name='Mehak'
employee2.name='Ashok'
employee3.name='Viren'
employee1.salary=40000
employee2.salary=50000
employee3.salary=60000

i=0
print('Salary of '+employee1.name+' is %i'%employee1.salary)
print('Salary of '+employee2.name+' is %i'%employee2.salary)
print('Salary of '+employee3.name+' is %i'%employee3.salary)

employee3._del_()





#Question 6
george_word=input("Enter the word, George\n")
barbie_word=input("Enter a new word using the same letter's as george's\n")
list_for_george_word=[]
list_for_barbie_word=[]
george_word.lower()
barbie_word.lower()


for i in george_word:
 list_for_george_word.append(i)
 list_for_george_word.sort()
for j in barbie_word:
 list_for_barbie_word.append(j)
 list_for_barbie_word.sort()
 
 
m=0
bool1=True
while((bool1==True)and(m<(len(george_word)))):
 bool1=(list_for_george_word[m]==list_for_barbie_word[m])
 m=m+1
 
 
if(m==(len(george_word))):
 print("Their freindship is true")
else:
 print("Their freindship is fake")



