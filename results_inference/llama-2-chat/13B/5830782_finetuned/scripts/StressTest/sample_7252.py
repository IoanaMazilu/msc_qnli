innings_premise = 5
innings_hypothesis = 8

# the hypothesis refers to the number of innings mentioned in the premise
if innings_hypothesis <= innings_premise:
    # check if the number of innings in the hypothesis contradicts the estimate of more than 'innings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of innings
    # any number of innings greater than 'innings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)