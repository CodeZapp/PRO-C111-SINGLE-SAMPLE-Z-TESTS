import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv
df = pd.read_csv('mediumData.csv')
data = df['reading_time'].tolist()
def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
meanList = []
for i in range(0, 1000):
    setOfMeans= randomSetOfMean(100)
    meanList.append(setOfMeans)
stdDeviation = statistics.stdev(meanList)
mean = statistics.mean(meanList)
print('Mean of sampling distribution:- ', mean)
print('Standard deviation of sampling distribution:- ', stdDeviation)
firstStdDeviationStart, firstStdDeviationEnd = mean - stdDeviation, mean + stdDeviation
secondStdDeviationStart, secondStdDeviationEnd = mean - (2 * stdDeviation), mean + (2 * stdDeviation)
thirdSstdDeviationStart, thirdStdDeviationEnd = mean - (3 * stdDeviation), mean + (3 * stdDeviation)
df = pd.read_csv('sample1.csv')
data = df['reading_time'].tolist()
meanOfSample1 = statistics.mean(data)
print('Mean of sample1:- ', meanOfSample1)
fig = ff.create_distplot([meanList], ['Student marks'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y=[0, 1.4], mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [meanOfSample1, meanOfSample1], y = [0, 1.4], mode = 'lines', name = 'MEAN OF STUDENTS WHO HAD MATH LABS'))
fig.add_trace(go.Scatter(x = [firstStdDeviationEnd, firstStdDeviationEnd], y = [0, 1.4], mode = 'lines', name = 'STANDARD DEVIATION 1 END'))
fig.add_trace(go.Scatter(x = [secondStdDeviationEnd, secondStdDeviationEnd], y = [0, 1.4], mode = 'lines', name = 'STANDARD DEVIATION 2 END'))
fig.add_trace(go.Scatter(x = [thirdStdDeviationEnd, thirdStdDeviationEnd], y = [0, 1.4], mode = 'lines', name = 'STANDARD DEVIATION 3 END'))
fig.show()
df = pd.read_csv('sample2.csv')
data = df['reading_time'].tolist()
meanOfSample2 = statistics.mean(data)
print('Mean of sample 2:- ', meanOfSample2)
fig = ff.create_distplot([meanList], ['Student marks'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1.4], mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [meanOfSample2, meanOfSample2], y = [0, 1.4], mode = 'lines', name = 'MEAN OF STUDENTS WHO USED THE APP'))
fig.add_trace(go.Scatter(x = [firstStdDeviationEnd, firstStdDeviationEnd], y = [0, 1.4], mode = 'lines', name = 'STANDARD DEVIATION 1 END'))
fig.add_trace(go.Scatter(x = [secondStdDeviationEnd, secondStdDeviationEnd], y = [0, 1.4], mode = 'lines', name = 'STANDARD DEVIATION 2 END'))
fig.add_trace(go.Scatter(x = [thirdStdDeviationEnd, thirdStdDeviationEnd], y = [0, 1.4], mode = 'lines', name = 'STANDARD DEVIATION 3 END'))
fig.show()
df = pd.read_csv('sample3.csv')
data = df['reading_time'].tolist()
meanOfSample3 = statistics.mean(data)
print('Mean of sample 3:- ', meanOfSample3)
fig = ff.create_distplot([meanList], ['student marks'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1.4], mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [meanOfSample3, meanOfSample3], y = [0, 1.4], mode = 'lines', name = 'MEAN OF STUDNETS WHO WERE ENFORCED WITH MATH REGISTERS'))
fig.add_trace(go.Scatter(x = [secondStdDeviationEnd, secondStdDeviationEnd], y=[0, 1.4], mode = 'lines', name = 'STANDARD DEVIATION 2 END'))
fig.add_trace(go.Scatter(x = [thirdStdDeviationEnd, thirdStdDeviationEnd], y = [0, 1.4], mode = 'lines', name = 'STANDARD DEVIATION 3 END'))
fig.show()
zScore = (mean - meanOfSample2) / stdDeviation
print('The z score is =', zScore)