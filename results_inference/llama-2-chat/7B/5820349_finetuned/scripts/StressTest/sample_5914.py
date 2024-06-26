tests_premise = 4
tests_hypothesis = 3
average_score_premise = 90
average_score_hypothesis = 90

# the hypothesis refers to the number of tests and average score mentioned in the premise
if tests_hypothesis >= tests_premise:
    # check if the number of tests in the hypothesis contradicts the premise (less than 4 tests)
    label = "contradiction"
elif average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests less than 'tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
