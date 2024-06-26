average_score_premise = 50
average_score_hypothesis = 50
tests_premise = 6
tests_hypothesis = 4

# the hypothesis refers to the average test score and the number of tests mentioned in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif tests_hypothesis >= tests_premise:
    # check if the number of tests in the hypothesis contradicts the estimate of less than 'tests_premise' tests
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests less than 'tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
