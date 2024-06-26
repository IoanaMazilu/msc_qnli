ration_premise = 2/4/6
ration_hypothesis = 2600

# the hypothesis refers to the number of people in the ration mentioned in the premise
if ration_hypothesis <= ration_premise:
    # check if the estimate of 'ration_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people in the ration
    # any number of people greater than 'ration_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)