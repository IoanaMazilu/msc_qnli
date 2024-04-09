racetrack_premise = 3
racetrack_hypothesis = 4

# the hypothesis refers to the number of fastest horses to be submitted to the Kentucky Derby
if racetrack_hypothesis <= racetrack_premise:
    # check if the hypothesis value contradicts the number of fastest horses in the premise
    label = "contradiction"
elif racetrack_hypothesis > racetrack_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives a specific number of fastest horses to be submitted, while the hypothesis gives a less specific estimate
    # any number of fastest horses less than or equal to 4 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
