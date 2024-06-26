premise_scores = [55, 67, 76, 82, 85]
hypothesis_scores = [35, 67, 76, 82, 85]

# the hypothesis refers to the same subjects as the premise
if hypothesis_scores == premise_scores:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any number of scores greater than 'premise_scores' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
