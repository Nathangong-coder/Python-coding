day_counter=0 #counter of how many times it was gone through the loop
birth_month=11 # this is the month of which I was born
birth_date=13 #this is the day of which I was born

def myfunction():
    for month_count in range(0,birth_month):
        print(end='.')#end makes it print on the same line
    print('')

while day_counter<birth_date: #while loop, when the day counter is less than my birth date, then it runs below code
    print(end='echo1') #while the day counter is less and criteria met, echo1 is printed.
    day_counter+=1 #add 1 to the counter  
    myfunction()

#you should state variables inside your function if you are ONLY using them inside the function, same with loops, that way python can clean up the variable