test_score_premise = 50
test_score_hypothesis = 50

# the hypothesis talks about the average test score of Joe, which is also referred to in the premise
if test_score_hypothesis <= test_score_premise:
    # check if the hypothesis value contradicts the estimate of the test score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the test score, and any value consistent with that estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
