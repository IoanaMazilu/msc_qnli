tests_premise = 4
tests_hypothesis = 3

# the hypothesis refers to the number of tests in the premise
if tests_hypothesis >= tests_premise:
    # check if the estimate of 'tests_hypothesis' contradicts the number of tests in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests less than 'tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
