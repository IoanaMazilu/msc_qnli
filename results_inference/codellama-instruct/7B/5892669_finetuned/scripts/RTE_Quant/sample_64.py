average_victims_per_day_premise = 8000
total_victims_hypothesis = 800000
total_days_premise = 100

# the hypothesis talks about the total number of victims in Rwanda, which is also mentioned in the premise
# but the premise does not provide a total number of victims, only the average number per day and the total days
# we cannot infer the total number of victims from the premise
label = "neutral"

print(label)
