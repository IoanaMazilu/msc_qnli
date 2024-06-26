distance_premise = 100
distance_hypothesis = 100
time_premise = 7
time_hypothesis = 8

# the hypothesis refers to the time taken for the journey, which is also mentioned in the premise
if time_hypothesis <= time_premise:
    # check if the estimate of 'time_hypothesis' contradicts the time taken in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken
    # any time taken greater than 'time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
