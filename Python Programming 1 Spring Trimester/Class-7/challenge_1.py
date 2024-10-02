#EPS 2022 Spring Trimester
#Programming 1- Ms. Lewellen
#Nathan Gong
#challenge_1
#for loop example
birth_month=11 #this is the month of which I was born
birth_day=13 #this is the day of which I was born
for day_count in range(0,birth_day): #for loop, when the day is in range from 0 to 13, then print it. day_counter is a counter. 
    print(end='echo') #printing the echo
    month_counter=0
    while month_counter<birth_month:
        print('.',end='')#print a space and a period after each echo, with the number of periods equal to birth month
        month_counter+=1
    print()
#While Loop Example
print('\n')
day_counter=0 #counter of how many times it was gone through the loop
birth_month=11 # this is the month of which I was born
birth_date=13 #this is the day of which I was born
while day_counter<birth_date: #while loop, when the day counter is less than my birth date, then it runs below code
    print(end='echo1') #while the day counter is less and criteria met, echo1 is printed.
    day_counter+=1 #add 1 to the counter
    for month_count in range(0,birth_month):
        print('.',end='')#end makes it print on the same line
    print('')


