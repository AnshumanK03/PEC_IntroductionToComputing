#ASSIGNMENT2


#Question1

st_input='Python is a case sensitive language'
a=len(st_input)                                              #len function to find the length of the given string
print('Length of the given input string:',a)
new_st = st_input[-1::-1]                                   #to reverse the order of the given string
print('String in reverse order:'+'"'+new_st+'"')
st1=st_input[10:26]                                          #Slicing the protion containing 'a case sensitive' from the given input string
print('New string in which case sensitive is stored:'+'"'+st1+'"')
st2 = st_input.replace('a case sensitive','object oriented')   #Replacing the substring 'a case sensitive' with 'object oriented'
print('New String after replacing "a case sensitive" by "object oriented":'+'"'+st2+'"')
index=st_input.find('a')                                      #Command to find the substring 'a' in   the input string
print('substring "a" appears at index:',index)
                                                          ## The following few lines of code are the process to remove blank spaces from the given input string,since strings are immutable,we use split function to first get different words separated by space and then use looping to add them to single string        
m=st_input.split()                                                                               
c=0                                               
nospaces=''
for word in m:
 nospaces=nospaces+m[c]
 c+=1
print('New string after removing spaces :',nospaces)


#Question2

name='Anshuman'                    #Storing name in a variable
SID=21103110                       #Storing SID in a variable
department='CSE'                   #Storing Department name in a variable
CGPA=9.9                           #Storing CGPA in a variable
print('Hey,',name+' Here!\nMy SID is %i'%SID+'\nI am from',department+' department and my CGPA is',CGPA)  ##Displaying the result according to the parameters in the question,\n for going to new line

#Question3

a=56                                
b=10
print('a&b:',a&b)
print('a|b:',a|b)
print('a^b:',a^b)
print('a<<2:',a<<2)                #Leftshift a by 2 bits
print('b<<2:',b<<2)                #Leftshift b by 2 bits
print('a>>2:',a>>2)                #Right shift a by 2 bits
print('b>>4:',b>>4)                #Right shift b by 4 bits


#Question4
#Basic algorithm to check maximum among 3 numbers using if else statement
greatest=0 
num1=int(input('Input number 1\n'))
num2=int(input('Input number 2\n'))
num3=int(input('Input number 3\n'))
if(num1>num2):      
 if(num1>num3):
  greatest=num1
 else:
  greatest=num3
else :
 if(num2>num3):
  greatest=num2
 else:
  greatest=num3
print('The greatest number is %i'%greatest)


#Question5
input_string=input('Input the string in which the substring "name" is to be searched in\n')
tosee='name'
m=tosee in input_string #Boolean variable to store the result whether the given substring "name" is present in the input_string or not
if(m==True):            #Based on the result of above boolean operation , displays whether or not the substring "name" is present in the given input string
 print('Yes,the input string contains  the word"name"')
else:
 print('No,the input string does not contain the word"name"')
 
 
#Question6
#A basic algorithm to check whether any of the sides is greater than the sum of either two , if yes then triangle is not possible , otherwise triangle is possible
length1=int(input('Input Side length 1\n'))
length2=int(input('Input side length 2\n'))
length3=int(input('Input side length 3\n'))
if((length1>length2+length3)|(length2>length1+length3)|(length3>length1+length2)):
 print('Triangle with the given sides is not possible')
else:
 print('Triangle with the given side is possible')



 
 


