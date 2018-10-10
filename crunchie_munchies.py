import numpy as np 

calorie_stats = np.genfromtxt('cereal.csv', delimiter = ',')
average_calories = np.mean(calorie_stats)
calorie_stats_sorted = np.sort(calorie_stats)

print (calorie_stats_sorted)
print (average_calories)

median_calories = np.median(calorie_stats)
print (median_calories)

#defines the 4th percentile- the value in the dataset at which 4% of the values are below it and the remaining 96% are above it
nth_percentile = np.percentile(calorie_stats, 4)
print (nth_percentile)

#the percentage of values in the dataset that are greater than 60
more_calories = np.mean(calorie_stats > 60)
print (more_calories)

calorie_std = np.std(calorie_stats)
print (calorie_std)