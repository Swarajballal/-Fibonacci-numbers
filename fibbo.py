#Python program to generate Fibonacci series 
a = 0  
b = 1  
count = 0    
print ("The fibonacci sequence of the numbers is:")  
while (count<=b):  
      print(a)
      count += 1  
      c = a + b   
      a = b 
      b = c
