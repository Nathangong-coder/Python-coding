import pandas as pd

#creating a series of classes, which is indexed by each period's corresponding letter
classes=pd.Series(["Topics","Spanish_2", "History", "Literature", "Chemistry", "Free", "Paper_Engineering", "Calculus"], index=["A", "B", "C", "D", "E", "F","G","H"])

#prints all the data in the series
print(classes)

#prints the D & F period data from the series
print("\nD period class:",classes.loc["D"])
print("F period class:", classes.loc["F"])


#creating a dataframe of my friend's names & other data

friends=pd.DataFrame({
    "last_name":["Pannoni", "Smolyanskiy", "Oberoi", "Ghorai"],
    "favorite_food":["Sushi", "Banana", "Dumplings", "Celery"],
    "A_period_class":["Topics", "Topics", "Topics", "Topics"],
    "favorite_number":[2,7,11,68],
}, index=["Miles", "Sasha", "Nihaal", "Soren"])

#prints the 1st row & 2nd to last row
print("\nfriends_first_row:",friends.iloc[0])
print("\nfriends_2nd_to_last_row:",friends.iloc[-2])

#prints a selected row by index name 
print("\nNihaal:",friends.loc["Nihaal"])

# for the number column calculate and print out the mean, min, and max for all values in the column
fav_num=friends.loc[:,"favorite_number"]
print("\n\nFavorite Number Statistics:")
print("mean:",fav_num.mean())
print("min:", fav_num.min())
print("max:",fav_num.max())
