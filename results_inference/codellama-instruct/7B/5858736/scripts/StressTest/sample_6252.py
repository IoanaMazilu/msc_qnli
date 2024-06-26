premise_scores = [1, 2, 3, 4]
hypothesis_scores = [1, 2, 3, 4]

# the hypothesis refers to the scores mentioned in the premise
if hypothesis_scores <= premise_scores:
    # check if the estimate of 'hypothesis_scores' contradicts the scores in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any number of scores greater than 'premise_scores' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
