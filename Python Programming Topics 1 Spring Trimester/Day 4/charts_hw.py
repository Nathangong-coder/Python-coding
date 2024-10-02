import matplotlib.pyplot as plt
import seaborn as sns

#CHALLENGE 1

#rows and columns for subplot
#all caps = constant, cannot be changed variable
SUBPLOT_ROW = 2
SUBPLOT_COLUMN = 2

#load the anscombe data set
#this isi data created by a statistician
#for different data visualizations
anscombe_df = sns.load_dataset("anscombe")

#extract dataset=="I" into a smaller dataframe
dataset1 = anscombe_df[anscombe_df.loc[:,"dataset"]=='I']
print(dataset1)

#extract dataset=="II" into a smaller dataframe
dataset2=anscombe_df[anscombe_df.loc[:,"dataset"]=='II']

#extract dataset=="III" into a smaller dataframe
dataset3=anscombe_df[anscombe_df.loc[:,"dataset"]=='III']

#extract dataset=="IV" into a smaller dataframe
dataset4=anscombe_df[anscombe_df.loc[:,"dataset"]=='IV']

#create a figure for subplots
fig = plt.figure()

#now add subplots
subplot1=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN, 1)
subplot2=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN, 2)
subplot3=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN, 3)
subplot4=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN, 4)

#plot subplot 1
subplot1.set_title("dataset 1")
subplot1.set_xlabel("x value")
subplot1.set_ylabel("y value")
subplot1.plot(dataset1.loc[:,"x"],dataset1.loc[:,"y"],"o")


#plot subplot 2
subplot2.set_title("dataset 2")
subplot2.set_xlabel("x value")
subplot2.set_ylabel("y value")
subplot2.plot(dataset2.loc[:,"x"],dataset2.loc[:,"y"],"o")
#plot subplot 3 & 4
subplot3.set_title("dataset 3")
subplot3.set_xlabel("x value")
subplot3.set_ylabel("y value")
subplot3.plot(dataset3.loc[:,"x"],dataset3.loc[:,"y"],"o")

subplot4.set_title("dataset 4")
subplot4.set_xlabel("x value")
subplot4.set_ylabel("y value")
subplot4.plot(dataset4.loc[:,"x"],dataset4.loc[:,"y"],"o")

#add main title
fig.suptitle("Anscombe data charts")
fig.tight_layout()
plt.show()







