average_tests_premise = 9
average_tests_hypothesis = 2

# the hypothesis refers to the number of tests in the premise
if average_tests_hypothesis <= average_tests_premise:
    # check if the hypothesis value contradicts the number of tests in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests greater than 'average_tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
