people_ratio_premise = 2:4:6
people_ratio_hypothesis = 6600

# the hypothesis refers to the number of people in the ratio mentioned in the premise
if people_ratio_hypothesis <= people_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_ratio_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
