chiefs_premise = 4
chiefs_hypothesis = 5

# the hypothesis refers to a different number of Joint Chiefs of Staff compared to the premise
if chiefs_hypothesis <= chiefs_premise:
    # check if the estimate of 'chiefs_hypothesis' contradicts the number of Joint Chiefs of Staff in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Joint Chiefs of Staff
    # any number of Joint Chiefs of Staff greater than 'chiefs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
