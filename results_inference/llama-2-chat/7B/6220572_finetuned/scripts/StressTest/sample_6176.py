commute_time_walk_premise = 15
commute_time_walk_hypothesis = 15

# the hypothesis refers to the difference in commute time between walking and train, also referenced in the premise
if commute_time_walk_hypothesis <= commute_time_walk_premise:
    # check if the hypothesis value contradicts the estimate of more than 'commute_time_walk_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference in commute time
    # any difference in commute time greater than 'commute_time_walk_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
