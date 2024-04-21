#password using python
import random 
upper= 'SAMRIDHI'
lower = 'sinha'
number='123456789'
symbols='!@#$%^&*'
string=upper+lower+number+symbols
length=5
password="".join(random.sample(string,length))
print('your password' +password)
