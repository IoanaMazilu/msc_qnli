death_rate_premise = 4
death_rate_hypothesis = 5
left_rate_premise = 15
left_rate_hypothesis = 15

# the hypothesis refers to the death and leaving rates mentioned in the premise
if death_rate_hypothesis <= death_rate_premise:
    # check if the death rate in the hypothesis contradicts the death rate in the premise
    label = "contradiction"
elif left_rate_hypothesis!= left_rate_premise:
    # check if the leaving rate in the hypothesis contradicts the leaving rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the death rate
    # any death rate greater than 'death_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
