chiefs_premise = 2
chiefs_hypothesis = 6

# the hypothesis discusses the same meeting with Joint Chiefs of Staff mentioned in the premise
if chiefs_hypothesis <= chiefs_premise:
    # check if the number of chiefs in the hypothesis contradicts the number of chiefs in the premise
    label = "contradiction"
else:
    # the premise provides only an estimate for the number of chiefs
    # any number of chiefs greater than 'chiefs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
