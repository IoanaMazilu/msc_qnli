premise_scores = [78, 82, 85]
hypothesis_scores = [78, 82, 85, 90]

# the hypothesis refers to the number of tests mentioned in the premise
if len(hypothesis_scores) <= len(premise_scores):
    # check if the hypothesis value contradicts the estimate of more than 'premise_scores'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests greater than 'premise_scores' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
