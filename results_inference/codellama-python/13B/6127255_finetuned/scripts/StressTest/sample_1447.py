death_rate_premise = 4
death_rate_hypothesis = 5
flee_rate = 15

# the hypothesis refers to the death and flee rates mentioned in the premise
if death_rate_hypothesis <= death_rate_premise:
    # check if the death rate in the hypothesis contradicts the death rate in the premise
    label = "contradiction"
elif flee_rate!= flee_rate:
    # check if the flee rate in the hypothesis contradicts the flee rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the death rate
    # any death rate greater than 'death_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
