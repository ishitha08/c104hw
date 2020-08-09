import statistics
import pandas as pd
import plotly_express as px
import random
import csv

df = pd.read_csv('data.csv')

height_list = df['Height(Inches)'].to_list()
weight_list = df['Weight(Pounds)'].to_list()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

print('mean,median,mode is {},{},{} respectively'.format(height_mean,height_median,height_mode))
print('mean,median,mode is {},{},{} respectively'.format(weight_mean,weight_median,weight_mode))