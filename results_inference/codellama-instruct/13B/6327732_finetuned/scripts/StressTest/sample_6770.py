ration_premise = 2:4:6
ration_hypothesis = 2:4:6

# the hypothesis refers to the ration of 2:4:6 mentioned in the premise
if ration_hypothesis <= ration_premise:
    # check if the estimate of 'ration_hypothesis' contradicts the ration in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ration
    # any ration greater than 'ration_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
