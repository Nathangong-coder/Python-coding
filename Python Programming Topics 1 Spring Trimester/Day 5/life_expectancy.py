import pandas as pd
import matplotlib.pyplot as plt

SUBPLOT_ROW = 1
SUBPLOT_COLUMN = 3

#data from www.gapminder.org
#data to revolutionize people's worldview
#this one contains global data about population,/ life exp, and GDP
gap_df = pd.read_csv("Python Programming Topics 1 Spring Trimester\Day 5\gapminder.tsv", sep='\t')
fig=plt.figure()

#print statements to explore the data
print(gap_df.info())
print(gap_df.head())
print(gap_df.tail())

#how to grab multiple columns
subset_df = gap_df.loc[:,["year","pop", "country"]]
print(subset_df)

#group by year and life expectancy
grouped_year_life_sg = gap_df.groupby("year")["lifeExp"]
print(grouped_year_life_sg)

#group by mean
print(grouped_year_life_sg.mean())
print(grouped_year_life_sg.aggregate(["mean", "max", "min"]))

#multiple group grouping
#life expectancy per year, per continent
life_yr_cont_sg=gap_df.groupby(["year", "continent"])["lifeExp"]
print(life_yr_cont_sg.aggregate(["mean", "max", "min"]),"\n")

#lifeExp + gdp, per year per continent
life_gdp_yr_cont_sg=gap_df.groupby(["year", "continent"])[["lifeExp","gdpPercap"]]
print(life_gdp_yr_cont_sg.aggregate(["mean", "max", "min"]))

#let's chart grouped data
yr_life_df=grouped_year_life_sg.aggregate(["mean"])
print(yr_life_df)

#get max and min values from the df
global_life=gap_df.loc[:,"lifeExp"]
min_life=global_life.min()
max_life=global_life.max()

global_life_plot = fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN, 1)
#set the limits of y axis
global_life_plot.set_ylim(min_life,max_life)
global_life_plot.plot(yr_life_df)
#add title & labels
global_life_plot.set_title("global life expectancy")
global_life_plot.set_xlabel("year")
global_life_plot.set_ylabel("life expectancy (years)")



#CHALLENGE 1
algeria_df=gap_df[gap_df.loc[:,"country"]=="Algeria"]
algeria_sg=algeria_df.groupby("year")["lifeExp"]
algeria_lifeExp_df=algeria_sg.aggregate(["mean"])
algeria_plot=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN,2)
algeria_plot.set_ylim(min_life,max_life)
algeria_plot.plot(algeria_lifeExp_df)
algeria_plot.set_title("Algerian life expectancy")
algeria_plot.set_xlabel("year")
algeria_plot.set_ylabel("life expectancy (years)")

#CHALLENGE 2

#grabbed continent data of Asia
asia_df=gap_df[gap_df.loc[:,"continent"]=="Asia"]

#grabbed lifeExp by year
asia_sg=asia_df.groupby("year")["lifeExp"]

#got mean, max and min life exp each year
asia_lifeExp_avg_df=asia_sg.aggregate(["mean"])
asia_lifeExp_max_df=asia_sg.aggregate(["max"])
asia_lifeExp_min_df=asia_sg.aggregate(["min"])

#added asia as subplot + set yLim
asia_plot=fig.add_subplot(SUBPLOT_ROW,SUBPLOT_COLUMN,3)
asia_plot.set_ylim(min_life,max_life)

#set title + labels
asia_plot.set_title("Asian life expectancy")
asia_plot.set_xlabel("year")
asia_plot.set_ylabel("life expectancy (years)")

#plots + made legend
asia_plot.plot(asia_lifeExp_avg_df)
asia_plot.plot(asia_lifeExp_min_df)
asia_plot.plot(asia_lifeExp_max_df)
asia_plot.legend(["mean","min","max"],loc="lower right", borderpad=0.25)

plt.tight_layout()
plt.show()