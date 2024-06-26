test_scores_premise = 60
test_scores_hypothesis = 60

# the hypothesis refers to the number of tests in the premise
if test_scores_hypothesis <= test_scores_premise:
    # check if the hypothesis value contradicts the number of tests in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests greater than 'test_scores_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
