test_score_premise = 50
test_score_hypothesis = 50

# the hypothesis talks about the number of tests, which is also mentioned in the premise
if test_score_hypothesis <= test_score_premise:
    # check if the hypothesis value contradicts the estimate of 'test_score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests less than 'test_score_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
