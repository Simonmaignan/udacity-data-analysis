# Loan Data from Prosper

## Dataset

The data consists of information regarding 113,937 loans, including 81 variables like loan status, borrower rate, loan original date, loan and other information about the loan and borrower. The dataset can be found [here](https://www.google.com/url?q=https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv&sa=D&ust=1554486256021000),
with the Prosper Data Dictionary to Explain Dataset's Variables [here](https://www.google.com/url?q=https://docs.google.com/spreadsheet/ccc?key%3D0AllIqIyvWZdadDd5NTlqZ1pBMHlsUjdrOTZHaVBuSlE%26usp%3Dsharing&sa=D&ust=1554486256024000).

## Data analysis process

### Data wrangling
In a first part, I wrangled the data in the data_wrangling Jupyter notebook. In this part,
* I had an overview of the different variable and chose 12 of them to analyze
* I tidied and cleaned the data set, composed of the 12 chosen variable to facilitate the exploratory phase

### Data exploration
In this second part I performed 2 distincts data explorations:
* I first performed a univariate exploration of each one of the variable
* Afterwards, I performed a bi and multi variate exploration of the variable by focusing on the relationship between the variables and especially the loan status and the borrower rate to try to explain which variables had an influence on those 2 special variables.

### Data explanation


## Summary of Findings

In the exploration, I found that:
* There is a correlation between the borrower rate and the loan status. Loans which payments are stopped or which are past due, consistently have highers rate.
* People with past delinquencies have a higher chance to stop their payments and have higher rates.
* Someone that owns a house has more chance to have lower rate has slightly less chance of stopping their loan payments as someone that doesn't.
* Someone with at least one recommandation has more chances to have a lower rate.
* People with lower credit score have higher rate and higher chance of stopping their payments.
* Students and profession with lower wages (realtor, waiter...) have the highest payment stopped ratio and highest rate and that the profession with the highest salaries (judge, dentist, pilot) have the lower payment stopped ratio and lowest rate.
* Data set concerns the loan opened between 2007 and 2015. There were almost no opened loans between 2009 and 2011 and there was a boom of opened loan in 2014.
* The yearly average rate oscillate between 0.2 and 0.15 with its minimum in 2008 and its maximum in 2012.

Outside of the main variable of interest, I could notice that people that owns a house have a higher credit score.


## Key Insights for Presentation

For the presentation, I focus on just the influence of the four Cs of diamonds
and leave out most of the intermediate derivations. I start by introducing the
price variable, followed by the pattern in carat distribution, then plot the
transformed scatterplot.

Afterwards, I introduce each of the categorical variables one by one. To start,
I use the violin plots of price and carat across clarity. I'm only looking at
the clarity grade plot here since it's the clearest example of how the
categorical quality grades affect diamond pricing. The other two categorical
variables, cut and color, are covered afterwards, using point plots. I've made
sure to use different color palettes for each quality variable to make sure it
is clear that they're different between plots.
