victims_per_day_premise = 8000
total_days_premise = 100
total_victims_hypothesis = 800000

# the hypothesis talks about the total number of victims in Rwanda, which is not mentioned in the premise
# the premise only mentions the average number of victims per day and the total number of days
# we cannot infer the total number of victims from the premise, so the relation is neutral
label = "neutral"

print(label)
