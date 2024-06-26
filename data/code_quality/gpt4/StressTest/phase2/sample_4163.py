speed_premise = 60
speed_hypothesis = 60

# the hypothesis refers to the speed of Tom's drive mentioned in the premise
if speed_hypothesis > speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif speed_hypothesis == speed_premise:
    # if the speed in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives the exact speed
    # any speed less than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
