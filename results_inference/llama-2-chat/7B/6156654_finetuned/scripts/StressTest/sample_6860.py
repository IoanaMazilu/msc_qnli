miles_walked_premise = 4
miles_walked_hypothesis = 4
time_premise = 1.0
time_hypothesis = 1.0
rate_premise = miles_walked_premise / time_premise
rate_hypothesis = miles_walked_hypothesis / time_hypothesis

# the hypothesis refers to the same situation as the premise, but with a different condition
if rate_premise == rate_hypothesis:
    label = "entailment"
elif rate_premise < rate_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
