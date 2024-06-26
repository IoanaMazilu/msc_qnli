hours_per_day_premise = [5, 5, 5, 10, 10]
hours_per_day_hypothesis = [6, 6, 6, 10, 10]

# the hypothesis refers to the number of hours worked per day on specific days, which are also mentioned in the premise
if hours_per_day_hypothesis!= hours_per_day_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives an estimate for the number of hours worked per day on specific days
    # any number of hours worked per day that is consistent with the premise is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
