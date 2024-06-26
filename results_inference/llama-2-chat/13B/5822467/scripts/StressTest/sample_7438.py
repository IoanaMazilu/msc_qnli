racetrack_horses_premise = 4
racetrack_horses_hypothesis = 3

# the hypothesis refers to the number of horses to be submitted to the Kentucky Derby
if racetrack_horses_hypothesis <= racetrack_horses_premise:
    # check if the hypothesis value contradicts the estimate of 'racetrack_horses_premise'
    label = "contradiction"
elif racetrack_horses_hypothesis > racetrack_horses_premise:
    # the hypothesis value is greater than the estimate, but not contradicting it
    label = "entailment"
else:
    # the premise gives only an estimate for the number of horses to be submitted
    # any number of horses less than or equal to 3 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
