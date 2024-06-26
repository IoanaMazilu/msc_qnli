tests_premise = 6
tests_hypothesis = 4
test_scores_premise = 50
test_scores_hypothesis = 50

# the hypothesis talks about the number of tests and the average test score, referenced also in the premise
if tests_hypothesis >= tests_premise:
    # check if the hypothesis value contradicts the estimate of less than 'tests_premise' tests
    label = "contradiction"
elif test_scores_hypothesis!= test_scores_premise:
    # check if the average test score in the hypothesis contradicts the average test score reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests less than 'tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
