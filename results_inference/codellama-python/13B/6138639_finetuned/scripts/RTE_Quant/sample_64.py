average_victims_per_day_premise = 8000
total_days_premise = 100
total_victims_hypothesis = 800000

# the hypothesis talks about the total number of victims which is not referenced in the premise (the time period is not mentioned)
# the hypothesis cannot be entailed from the premise, since the total number of victims is unknown.
label = "neutral"

print(label)
