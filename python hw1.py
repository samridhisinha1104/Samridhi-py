#built in maths functions
print(abs(-25))
print(pow(2,4))
print(min(10,20,30,40,50))
print(max(10,20,30,40,50))
print(divmod(17,3))
print(bin(64),oct(64),hex(64))
print(round(2.567),round(2.5678,2))


s='bamboozled'
# extract B a
print(s[0],s[1])
print(s[-10],s[-9])
# extract e d
print(s[8],s[9])
print(s[-2],s[9])

#extract mboozled
print(s[2:10])
print(s[2:])
print(s[-8:])

#extract Bamboo
print(s[0:6])
print(s[:6])
print(s[-10:-4])
print(s[:-4])

#reverse Bamboolzed

ms= input('Enter martial status:')
s= input('Enter sex:')
age=int(input('Enter age:'))
if (ms =='m') or (ms=='u' and s=='m' and age>30)\
    or(ms=='u' and s=='f' and age>25):
        print('Insured')
else:
   print('Not Insured ') 
   
   #write a program that prints all unique combinations of 1,2 and 3 
i=1
while i<= 3:
    j=1
    while j<=3 :
        k=1
        while k<= 3:
            k=1
            while k<= 3:
                if i== j or j == k or k == i:
                    k+=1
                    continue
                else:
                    print(i,j,k)
                k+=1
            j+=1
        i+=1    
              
                
    


