time_difference_premise = 6
time_difference_hypothesis = 1

# the hypothesis refers to the time difference between Arun and Anil mentioned in the premise
if time_difference_hypothesis >= time_difference_premise:
    # check if the time difference in the hypothesis contradicts the time difference in the premise
    label = "contradiction"
else:
    # the premise gives an estimate of the time difference
    # any time difference less than 'time_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
