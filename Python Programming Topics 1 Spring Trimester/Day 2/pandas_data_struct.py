import pandas as pd

#let's do a class demo on pandas, a library for data analysis

#let's create a series of fruits
fruits=pd.Series(["orange", "pineapple", 'mango', "dragonfruit"])

#prints the full list
print(fruits)
#prints the first item in the list
print("fruits.iloc[0]:",fruits.iloc[0])
#prints the last time in the list 
print("fruits.iloc[-1]:",fruits.iloc[-1])

#create series with explicit index
student = pd.Series(["Miles Pannoni", "oranges", 16], index=["name", "favorite_fruit", "age"])

#select data from series via index value
print(student)
#finding and printing student's name
print("name: ", student.loc["name"])
#finding and printing student's age
print("age: ", student.loc["age"])



#let's create and work with dataframes

#creating a dataframe of family/friends
family=pd.DataFrame(
    {
    "first_name": ["Nathan", "Arthur", "Rui", "Amy"],
    "last_name": ["Gong", "Gong", "Gong", "Yuan"],
    "height": [72, 69, 72, 67],
    "age": [16, 14, 47,45]
    }
)

#print out dataframe
print(family)

#print out first person and last person using iloc
print("family first row:",family.iloc[0])
print("family last row:",family.iloc[-1])

#creating an indexed dataframe of family/friends
indexed_family=pd.DataFrame(
    {
    
    "last_name": ["Gong", "Gong", "Gong", "Yuan"],
    "height": [72, 69, 72, 67],
    "age": [16, 14, 47,45]
    },
    index=["Nathan", "Arthur", "Rui", "Amy"]
)

#grab rows of two names and print them out using loc
print(indexed_family)
print("Rui:", indexed_family.loc["Rui"])

#this is how we grab all the data from a certain column
#in this example we will grab age 
ages=indexed_family.loc[:, "age"]
heights = indexed_family.loc[:,"height"]
print("Ages: ", ages)
print("Heights: ", heights)

#aggregate functions
print("AGES")
print("mean:", ages.mean())
print("min:", ages.min())
print("max:",ages.max())

#aggregate functions for heights
print("HEIGHTS:")
print("mean:",heights.mean())
print("min:",heights.min())
print("max:",heights.max())