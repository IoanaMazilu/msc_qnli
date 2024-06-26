innings_premise = 14
innings_hypothesis = 84

# the hypothesis refers to the number of innings mentioned in the premise
if innings_premise >= innings_hypothesis:
    # check if the number of innings in the premise contradicts the estimate of less than 'innings_hypothesis'
    label = "contradiction"
else:
    # the premise gives only an exact number of innings
    # any number of innings less than 'innings_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
