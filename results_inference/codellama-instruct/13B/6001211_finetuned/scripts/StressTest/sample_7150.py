chiefs_premise = 4
chiefs_hypothesis = 5

# the hypothesis refers to the number of Joint Chiefs of Staff at a meeting mentioned in the premise
if chiefs_hypothesis <= chiefs_premise:
    # check if the number of chiefs in the hypothesis contradicts the estimate of more than 'chiefs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of chiefs
    # any number of chiefs greater than 'chiefs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
