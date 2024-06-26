test_scores_premise = [78, 82, 85, 90]
test_scores_hypothesis = [78, 82, 85]

# the hypothesis refers to the number of tests mentioned in the premise
if len(test_scores_hypothesis) < len(test_scores_premise):
    # check if the hypothesis value contradicts the number of tests in the premise
    label = "contradiction"
else:
    # calculate the arithmetic mean of the hypothesis values
    hypothesis_mean = sum(test_scores_hypothesis) / len(test_scores_hypothesis)
    # calculate the arithmetic mean of the premise values
    premise_mean = sum(test_scores_premise) / len(test_scores_premise)
    # check if the hypothesis mean is equal to the premise mean
    if hypothesis_mean == premise_mean:
        # if the hypothesis mean is equal to the premise mean, we can infer entailment
        label = "entailment"
    else:
        # if the hypothesis mean is not equal to the premise mean, we cannot infer entailment or contradiction
        label = "neutral"

print(label)
