#Nathan Gong
#Spring Trimester 2022, Prog 1
#Ms. Lewellen
#Midterm_2
#passing grade is 60 percent or more, failing grade is less than 60 percent 

user_percentage=input('Please choose a percentage from 0 to 100 ')
user_percent=int(user_percentage)

if 0<user_percent and user_percent<60:
    print('FAIL')
if 60<user_percent and user_percent<100:
    print('PASS')
elif user_percent>100 or user_percent<0:
    print('error error')