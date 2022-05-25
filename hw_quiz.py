points=0
q1='''Question 1:
What will be the output of the following code snippet?
# Code Snippet Starts
a = 10

def function(a):
    a = 20  
    print(a)
a = 23

function(a)
# Code Snippet Ends
_______x__________
 a) 10
 b) 20
 c) 23
 d) Error'''
print(q1)
qa1=input('what is the answer?: ')
if qa1 =='b':
    print('Absolutely correct😊!')
    points=points+1
elif qa1 =='a'or'c'or'd':
    print('Wrong ')    
else:
    print('Pls type a option')
print('score: ',points)        

q2='''Question 2:
What is the output of the following code snippet?
# Code Snippet Starts
num = 10
print(id(num))

# Code Snippet Ends
________x________
a) num
b) 10
c) 10105376
d) 1010'''
print(q2)
qa2=input('what is the answer?: ')
if qa2 =='c':
    print('Absolutely correct😊!')
    points=points+1
elif qa2 =='a'or'b'or'd':
    print('Wrong ')    
else:
    print('Pls type a option') 
print('score: ',points)       

q3='''Question 3:
What is the output of the following code and what is the type of function of print() call?
# Code Snippet Starts
value = 'Apple'
value2 = 'Pear'
val3 = value+value2
print(val3)

# Code Snippet Ends
a)ApplePear
b) Apple Pear
c) Apple
d) Pear'''
print(q3)
qa3=input('what is the answer?: ')
if qa3 =='a':
    print('Correct😃!')
    points=points+1
elif qa3 =='c'or'b'or'd':
    print('Wrong. Better luck next time')    
else:
    print('Pls type a option') 
print('score: ',points)       

q4='''Question 4:
What is the output of the following code snippet?

# Code Snippet Starts

s = 'Quiz-Orbit'

def retriveString(s):

    val = (“”).join(s.split(“-“))

    return val

print(retriveString(s))

# Code Snippet Ends
___________x_________
a) Quiz-Orbit
b) QuizOrbit
c) Quiz
d) Orbit'''
print(q4)
qa4=input('what is the answer?: ')
if qa4 =='b':
    print('Correct😃!')
    points=points+1
elif qa4 =='c'or'a'or'd':
    print('Wrong. Better luck next time')    
else:
    print('Pls type a option') 
print('score: ',points)     

q5='''Question 5:
What is the output of the following code?
# Code Snippet Starts

a = (3,4,5)
print(str(id(a))[:4])

# Code Snippet Ends

a) 3892
b) 1899
c) 1402
d) 3621'''
print(q5)
qa5=input('what is the answer?: ')
if qa5 =='c':
    print('Correct😃!')
    points=points+1
elif qa5 =='b'or'a'or'd':
    print('Wrong. Better luck next time')    
else:
    print('Pls type a option') 
print('score: ',points)     
