victims_per_day_premise = 8000
days_premise = 100
victims_hypothesis = 800000

# the hypothesis talks about the total number of victims, which is not mentioned in the premise
# the hypothesis cannot be entailed from the premise, since the total number of victims is unknown.
label = "neutral"

print(label)
