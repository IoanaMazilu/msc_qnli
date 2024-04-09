test_scores_premise = [82, 85, 78, 90, 80, 85, 75, 88, 80]
test_scores_hypothesis = [82, 85, 78, 90, 80, 85, 75, 88, 80]

# the hypothesis refers to the same set of test scores as the premise
if sum(test_scores_hypothesis) <= sum(test_scores_premise):
    # check if the estimate of 'test_scores_hypothesis' contradicts the sum of test scores in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average test score
    # any average test score greater than 'test_scores_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
