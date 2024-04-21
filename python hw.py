#create a list of 5 names 
names=['Anil','Amol','Aditya','Avi','Alka']
print(names)
# insert a names 'Anuj' before 'Aditya'
names.insert(2,'Anuj')
print(names)
# append a name 'zulu'
names.append('Zulu')
print(names)
    #Delete 'Avi' from the the list
names.remove('Avi')
print(names)
#Replace 'Anil' with 'Anil Kumar'
i=names.index('Anil')
names[i]='Anil Kumar'
print(names)
#print reversed sorted list
names.reverse()
print(names)

#Pass a tuple to the divmod() function and obtain the qoutient and the remainder 

result=divmod(17,3)
print(result)
t=(17,3)
result=divmod(*t)
print(result)

boys={'Nilesh':41,'Soumitra':42,'Nadeem':47}
girls={'Rasika':38,'Rajshree':43,'Rasika':45}
combined={**boys,**girls}
print(combined)
combined={**girls,**boys}
print(combined)

#create a calender 
import calender
year= int(input("enter the year"))
print(year)
month=int(input("enter your month"))
print(month)
x=calender.month(year,month)
print(x)