#Assignment 3

#Problem 1

print('Input a string')
st = str(input())
l=st.split() #Spliting the string to check further whether it has only single word or more than that
m=len(l)
charct=dict() #Dictionary to store the occurences of each character/word in front of that character/word
if(m==1):  #Case 1 when the string contains only one word
 chars = set(st) #We store the value of the word in set due to the property of set containing unique elements so that we can distinguish between unique elements and repeated ones
 for i in chars:
  charct[i]=0  #First setting the value of each occurence of unique elements as 0 which we will further add whenever that element comes in the word
 for i in st:  #Running the loop over every letter and counting the occurences of each unique element and storring in dictionary charct
  charct[i]=charct[i]+1
 print(charct)
#Same algorithm as in if clause except now we are treating words instead of characters
else:
 words=st.split()
 words_without_repition=set(words)
 for i in words_without_repition:
  charct[i]=0
 for i in l:
  charct[i]=charct[i]+1
 print(charct)
 
  
 

#Problem 2

day=int(input('Input the date '))
month=int(input('Input the month '))
year=int(input('Input the year '))
if((month>=1)&(month<=12)&(day>=1)&(day<=31)&(year>=1800)&(year<=2025)):
 if(((month==1)|(month==3)|(month==5)|(month==7)|(month==8)|(month==10)|(month==12))&(day<31)):
  day=day+1	
  print('Next date\n'+'Day %i'%day+'\n'+'Month %i'%month+'\n'+'Year %i'%year)
 elif(((month==1)|(month==3)|(month==5)|(month==7)|(month==8)|(month==10)|(month==12))&(day==31)):
  if(month==12):
   year=year+1
   day=1
   month=1
  else:
   day=1
   month=month+1
  print( 'Next date\n'+'Day %i'%day+'\n'+'Month %i'%month+'\n'+'Year %i'%year)
 elif(month==2):
  if((year%4==0)&(day<29)):
   day=day+1
   print('Next date\n'+'Day %i'%day+'\n'+'Month %i'%month+'\n'+'Year %i'%year)
  elif((year%4==0)&(day==29)):
   day=1
   month=month+1
   print('Next date\n'+'Day %i'%day+'\n'+'Month %i'%month+'\n'+'Year %i'%year)
  elif((year%4!=0)&(day<28)):
   day=day+1
   print('Next date\n'+'Day %i'%day+'\n'+'Month %i'%month+'\n'+'Year %i'%year)
  elif((year%4!=0)&(day==28)):
   day=1
   month=month+1
   print('Next date\n'+'Day %i'%day+'\n'+'Month %i'%month+'\n'+'Year %i'%year)
  else:
   print('Invalid Format')
 elif((month==4)|(month==6)|(month==9)|(month==11)&(day<30)):
  day=day+1
  print('Next date\n'+'Day %i'%day+'\n'+'Month %i'%month+'\n'+'Year %i'%year)
 elif(((month==4)|(month==6)|(month==9)|(month==11))&(day==30)):
  day=1
  month=month+1
  print('Next date\n'+'Day %i'%day+'\n'+'Month %i'%month+'\n'+'Year %i'%year)
else:
 print('Invalid Format')
 
 


#Problem 3

#Prompt for the user that asks user every time at the completion of loop whether or not to add further elements in the input list
loop_prompt='y'  
#Counter variable that counts the number of elements in the input list                                              
n=1  
#Tuples that will contain the element and its square in the output list                                                               
square_tuple=tuple()  
#Input list that will contain the elements that will be entered by the user                                           
element=list()                                                       

#while loop that will add the elements to the list as soon as they are input by the user
while(loop_prompt=='y'):
 print('Enter element number %i'%n)
 new_element=int(input()  )
 element.append(new_element)
 print('Enter y for continuing to add other elements and any other letter to stop')
 loop_prompt=str(input())     #Updating the loop prompt which will decide whether the loop will go further or not note that being case sensitive only y will carry the loop forward
 n=n+1
 
#Final loop that will form and print hte output list containing the squares of the elements of input list
output_list=[]
for i in element:
  square_tuple=(i,(i*i))
  output_list.append(square_tuple)
print('The output list containg the tuples of number and the square is')
print(output_list)




#Problem 4

print('Input the grade')
input_grade=int(input()) 

#The initial lists are defined in a systematic manner to avoid any confusion , these will be latter used to contain a list of respective row wise tuples of grades, refer to looping part for that
grade=[4,5,6,7,8,9,10]
performance=['Poor','Below Average','Average','Good','Very Good','Excellent','Outstanding']
letter_grade=['D','C','C+','B','B+','A','A+']
row_tuple=tuple()  #Row wise tuple for containing respective grade, performance,letter grade respectively
row_wise_list=list() #Row wise list for containg respective rows of grading
m=0


if((input_grade>=4)&(input_grade<=10)):   #Checking validity of grade
 for i in grade:
  row_tuple=(grade[m],performance[m],letter_grade[m])
  row_wise_list.append(row_tuple)
  m=m+1
 n=grade.index(input_grade)
 input_containing_row=row_wise_list[n]
 print('For Grade %i'%input_grade+' output is')
 print('Your Grade is %s'%input_containing_row[2]+' and %s'%input_containing_row[1]+' Performance')
else:
  print('Out of range')
 



#Problem 5

given_string='ABCDEFGHIJK'
m=len(given_string)
n=0
while(m>=1):
 print((' '*n)+given_string[:m])
 m=m-2 #Decrement of two letters from the back of the string for each progressive row
 n=n+1 #Increment of blank spaces in front of the string for each progressive row
 
 
 
 
#Problem 6

student_details=dict()
prompt='Y'
name_list=[]
sid_list=[]

while(prompt=='Y'):
 print('Input SID')
 sid=int(input())
 print('Input Name')
 name=str(input())
 student_details[sid]=name
 name_list.append(name)
 sid_list.append(sid)
 print('Press Y to continue and N to go back')
 prompt=str(input())
 
print('Student Details as sorted in dictionary are')
print(student_details)

name_list.sort()
sort_name=dict()
m=0

while(m<len(student_details)):
 for j in student_details:
  if(student_details[j]==name_list[m]):
   sort_name[j]=name_list[m]
 m=m+1
  
print('The dictionary sorted ot by name is')
print(sort_name)

sid_list.sort()
sort_sid=dict()
m=0

while(m<len(student_details)):
 for j in student_details:
  if(j==sid_list[m]):
   sort_sid[j]=student_details[j]
 m=m+1
  
print('The dictionary sorted out by sid is')
print(sort_sid)

print('Input the sid for which the details are to be searched')
input_sid=int(input())
for i in student_details:
 if(input_sid==i):
  print('The details of the student are as follows\nThe Sid is %i'%i+'\nAnd the name is %s'%student_details[i]) 
  
  
  
  
#Problem 7

a=0
b=1
print('Input the number of terms')   #Taking the input from the user till which term is the sequence to be displayed
n=int(input())
m=2
fibonacci=[0,1]                      #Creating a list of fibonacci numbers with 0 and 1 as initial two numbers , more to be added further
while(m<n):                          #Loop for adding fibonacci sequence to the list till the counter variable is less than the number of terms
 c=a
 a=b
 b=a+c
 fibonacci.append(b)
 m=m+1

print('The fibonacci series upto %i terms is'%n)
print(fibonacci)
#Printing the average of fibbonacci sequence until n terms
print('Average of the above fibonacci terms is')
print((sum(fibonacci))/m)




#Problem 8

set_1={1,2,3,4,5}     
set_2={2,4,6,8}
set_3={1,5,9,13,17}
#Note that the operations performed below give us the right answer because of the property of sets that no element can repeat itself
#Set4 which contains the elements that are present in Set 1 and Set 2 but not in both
set_4=set_1.union(set_2).difference(set_1.intersection(set_2))    
print('The set containing the elements in set 1 and set2 but not in both is')
print(set_4)
#Set5 is the set containing the elements in exactly one of the above sets
set_5=(((set_1.union(set_2.union(set_3))).difference(set_1.intersection(set_2))).difference(set_2.intersection(set_3))).difference(set_1.intersection(set_3)).difference(set_1.intersection(set_2.intersection(set_3)))
print('The set containing the elements in exactly one of the above given set is')
print(set_5)
set_6=set_1.intersection(set_2)
set_7=set_2.intersection(set_3)
set_8=set_1.intersection(set_3)
#set9 is the set containing the elements in exactly two of the above sets
set_9=(set_6.union(set_7)).union(set_8).difference(set_1.intersection(set_2.intersection(set_3)))
print('The set containing the elements in exactly two of the above given sets is')
print(set_9)
set_1to10={1,2,3,4,5,6,7,8,9,10}
set_10=set_1to10.difference(set_1)
set_11=set_1to10.difference((set_1.union(set_2)).union(set_3))
print('The set containg the elements in the range from 1 to 10 not in the set 1')
print(set_10)
print('The set containing the elements in the range from 1 to 10 not in the set1,set2 and set3')
print(set_11)

