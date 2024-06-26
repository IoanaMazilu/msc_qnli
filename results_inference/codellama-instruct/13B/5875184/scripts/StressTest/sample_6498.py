matthew_wake_premise = "t"
matthew_wake_hypothesis = "y"
johnny_walk_premise = "y"
johnny_walk_hypothesis = "t"

# the hypothesis refers to the distance traveled by Johnny
if johnny_walk_hypothesis <= johnny_walk_premise:
    # check if the estimate of 'johnny_walk_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled
    # any distance greater than 'johnny_walk_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
