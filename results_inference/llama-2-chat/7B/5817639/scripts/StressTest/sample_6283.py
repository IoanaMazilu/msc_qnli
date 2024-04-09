test_scores_premise = [82, 85, 78, 90, 80, 83, 75, 87, 82]
test_scores_hypothesis = [82, 85, 78, 90, 80, 83, 75, 87, 82]

# the hypothesis talks about the average test score of Robin on 9 tests, which is also mentioned in the premise
if sum(test_scores_premise) <= sum(test_scores_hypothesis):
    # check if the estimate of 'test_scores_hypothesis' contradicts the sum of the test scores in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average test score
    # any average test score greater than the sum of the test scores in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
