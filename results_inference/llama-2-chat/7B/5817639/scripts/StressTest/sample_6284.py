test_scores_premise = 82
test_scores_hypothesis = 82

# the hypothesis talks about the average test score of Robin on more than 9 tests
if test_scores_hypothesis <= test_scores_premise:
    # check if the hypothesis value contradicts the estimate of the average test score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average test score
    # any average test score greater than 'test_scores_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
