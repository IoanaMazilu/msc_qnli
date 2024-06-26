test_count_premise = 6
test_count_hypothesis = 4
average_score_premise = 50
average_score_hypothesis = 50

# the hypothesis talks about Joe's average test score and the number of tests, both referenced in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif test_count_hypothesis >= test_count_premise:
    # check if the number of tests in the hypothesis contradicts the estimate of less than 'test_count_premise' tests
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests less than 'test_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
