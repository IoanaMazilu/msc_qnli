average_score_premise = 82
tests_count_premise = 2
average_score_hypothesis = 82
tests_count_hypothesis = 9

# the hypothesis refers to the average test score and the number of tests mentioned in the premise
if average_score_premise!= average_score_hypothesis:
    # check if the average test score in the hypothesis contradicts the average test score reported in the premise
    label = "contradiction"
elif tests_count_hypothesis <= tests_count_premise:
    # check if the number of tests in the hypothesis contradicts the estimate of more than 'tests_count_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests greater than 'tests_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
