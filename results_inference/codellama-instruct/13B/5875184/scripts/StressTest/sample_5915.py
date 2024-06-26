premise_scores = [90, 80, 70]
hypothesis_scores = [90, 80, 70, 60]

# the hypothesis refers to the number of tests mentioned in the premise
if len(hypothesis_scores) > len(premise_scores):
    # check if the hypothesis value contradicts the estimate of more than 'len(premise_scores)' tests
    label = "contradiction"
elif hypothesis_scores[0]!= premise_scores[0]:
    # check if the hypothesis value contradicts the estimate of the first test score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests and the first test score
    # any number of tests greater than 'len(premise_scores)' and any first test score equal to 'premise_scores[0]' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
