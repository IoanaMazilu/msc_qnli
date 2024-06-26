score_test_premise = 83
score_test_hypothesis = 83

# the hypothesis talks about the average score on a certain number of tests, referenced also in the premise
if score_test_hypothesis == score_test_premise:
    # check if the hypothesis value contradicts the average score reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score
    # any average score equal to'score_test_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
