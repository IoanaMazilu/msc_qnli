joined_time_premise = 8
joined_time_hypothesis = 2

# the hypothesis refers to the time when Jose joined, mentioned in the premise
if joined_time_hypothesis >= joined_time_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
else:
    # the premise gives an estimate for the time when Jose joined
    # any time less than 'joined_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
