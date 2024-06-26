robin_test_premise = 10
robin_test_hypothesis = 30

# the hypothesis talks about the number of tests, referenced also in the premise
if robin_test_hypothesis <= robin_test_premise:
    # check if the hypothesis value contradicts the estimate of 'robin_test_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests greater than 'robin_test_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
