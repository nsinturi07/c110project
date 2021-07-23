import pandas as pd
import csv
import random
import statistics
import plotly.figure_factory as ff

df=pd.read_csv("data")
data=df["temp"].tolist()
#chart=ff.create_distplot([data], ["temp"], show_hist=False)
#standarddeviation=statistics.mean(data)
#populationmean=statistics.stdev(data)
#print(populationmean, standarddeviation)
#chart.show()
def random_mean(counter):
    temp=[]
    
    for i in range(0,counter):
        random_temp=random.randint(0,len(data))
        value=data[random_temp]
        temp.append(value)
    #standarddeviation=statistics.stdev(temp)
    mean=statistics.mean(temp)
    return(mean)
#print(standarddeviation, mean)
def showtemp(meanlist):
    df=meanlist
    chart=ff.create_distplot([df], ["temp"], show_hist=False)
    chart.show()
def main():
    meanlist=[]
    for i in range(0,1000):
        randommean=random_mean(100)    
        meanlist.append(randommean)
    showtemp(meanlist)
main()
