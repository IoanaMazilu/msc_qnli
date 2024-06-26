average_score_premise = 60
average_score_hypothesis = 60
tests_premise = 2
tests_hypothesis = 4

# the hypothesis refers to the average test score and number of tests mentioned in the premise
if average_score_hypothesis != average_score_premise:
    # check if the 'average_score_hypothesis' contradicts the average score in the premise
    label = "contradiction"
elif tests_hypothesis <= tests_premise:
    # check if the number of tests in the hypothesis contradicts the estimate of more than 'tests_premise' tests
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests more than 'tests_premise' with the same average score is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
