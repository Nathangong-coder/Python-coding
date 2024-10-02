import matplotlib.pyplot as plt
import seaborn as sns

#CHALLENGE 0: Tutorial for advcharts

#rows and columns for subplot
#all caps = constant, cannot be changed variable
SUBPLOT_ROW = 2
SUBPLOT_COLUMN = 3

#load restaurant data & explore it
tips_df= sns.load_dataset("tips")
print(tips_df.head())
#get value counts of a column
tips_by_gender= tips_df.loc[:,"sex"].value_counts()
print(tips_by_gender)


#figure of 10 x 6 inches
fig = plt.figure(figsize=(10,6))

#create a histogram
#data in total bill amounts
total_bills = tips_df.loc[:,"total_bill"]
#draw the histogram
hist_plot = fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN, 1)
hist_plot.hist(total_bills, bins=10, color="lightblue", ec="black")
hist_plot.set_title("histogram of total bills")
hist_plot.set_xlabel("total bill bins")
hist_plot.set_ylabel("total bill")

#scatter plot
tips = tips_df.loc[:,"tip"]
#draw the scatter plot
scatter_plot=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN,2)
scatter_plot.scatter(total_bills, tips)
#add title, x and y labels
scatter_plot.set_title("Scatter Plot of Bills vs Tips")
scatter_plot.set_xlabel("Total Bills")
scatter_plot.set_ylabel("Tips")
#box plot
#grab lunch and dinner
lunch_df=tips_df[tips_df.loc[:,"time"]=="Lunch"]
dinner_df=tips_df[tips_df.loc[:,"time"]=="Dinner"]
#from these, grab the tips
lunch_tips = lunch_df.loc[:,"tip"]
dinner_tips = dinner_df.loc[:,"tip"]


#plot location of box plot
box_plot=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN,3)
#add title, x and y labels
box_plot.set_title("Box Plot of Lunch vs Dinner")
box_plot.set_xlabel("Category")
box_plot.set_ylabel("Tip")
#draw boxplot
box_plot.boxplot([lunch_tips,dinner_tips], labels=["Lunch", "Dinner"])

#CHALLENGE 2
hist_2_plot=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN,4)
hist_2_plot.hist(tips,bins=10,color="lightgreen", ec="black")
hist_2_plot.set_title("Histogram of total tips")
hist_2_plot.set_xlabel("total tip bins")
hist_2_plot.set_ylabel("total tip")

#CHALLENGE 3
scatter_2_plot=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN,5)
size=tips_df["size"]
scatter_2_plot.scatter(tips,size)
#add title, x and y labels
scatter_2_plot.set_title("Scatter Plot of Size vs Tips")
scatter_2_plot.set_xlabel("Tips")
scatter_2_plot.set_ylabel("Size")
#CHALLENGE 4

#grab stats for smoker and non-smoker
smoker_df=tips_df[tips_df.loc[:,"smoker"]=="Yes"]
non_smoker_df=tips_df[tips_df.loc[:,"smoker"]=="No"]
#from these, grab the tips
non_smoker_tips = non_smoker_df.loc[:,"tip"]
smoker_tips = smoker_df.loc[:,"tip"]

box_2_plot=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN,6)

#add title, x and y labels
box_2_plot.set_title("Big Box Plot")
box_2_plot.set_xlabel("Category")
box_2_plot.set_ylabel("Tip")

#draw boxplot
box_2_plot.boxplot([lunch_tips,dinner_tips,smoker_tips,non_smoker_tips], labels=["Lunch", "Dinner","Smoker", "Non-Smoker"])








plt.tight_layout()
plt.show()