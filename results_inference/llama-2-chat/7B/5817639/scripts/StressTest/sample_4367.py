x_per_hour_premise = 50
x_per_hour_hypothesis = 60

# the hypothesis refers to the pay rate for more than 40 hours worked in a week
if x_per_hour_hypothesis <= x_per_hour_premise:
    # check if the estimate of 'x_per_hour_hypothesis' contradicts the pay rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the pay rate, and any pay rate greater than 'x_per_hour_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
