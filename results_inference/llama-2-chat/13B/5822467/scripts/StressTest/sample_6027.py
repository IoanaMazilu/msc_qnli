joe_test_scores_premise = 50
joe_test_scores_hypothesis = 50

# the hypothesis refers to the average test score of Joe in less than 6 tests
if joe_test_scores_hypothesis <= joe_test_scores_premise:
    # check if the hypothesis value contradicts the estimate of the premise
    label = "contradiction"
else:
    # the premise gives a specific value for the average test score of Joe
    # any lower value for the number of tests is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
