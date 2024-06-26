time_premise = 8
time_hypothesis = 6

# the hypothesis refers to the time after which Tom goes, which is also mentioned in the premise
if time_hypothesis <= time_premise:
    # check if the estimate of 'time_hypothesis' contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time after which Tom goes
    # any time greater than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
