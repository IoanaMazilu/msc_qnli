premise_scores = [45, 67, 76, 82, 85]
hypothesis_scores = [55, 67, 76, 82, 85]

# the hypothesis refers to the exact scores obtained by Reeya in different subjects
if hypothesis_scores == premise_scores:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores obtained by Reeya
    # any number of scores greater than or equal to the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
