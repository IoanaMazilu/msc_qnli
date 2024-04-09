average_score_premise = 83
average_score_hypothesis = 83
test_score_premise = 10
test_score_hypothesis = 70

# the hypothesis refers to Robin's average score and the score of a specific test mentioned in the premise
if average_score_premise!= average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif test_score_hypothesis <= test_score_premise:
    # check if the hypothesis value contradicts the estimate of less than 'test_score_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the test score
    # any test score less than 'test_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
