robin_score_premise = 82
robin_score_hypothesis = 82
num_tests_premise = 9

# the hypothesis talks about the number of tests, referenced also in the premise
if num_tests_premise <= robin_score_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'robin_score_premise'
    label = "contradiction"
elif robin_score_hypothesis!= robin_score_premise:
    # check if the hypothesis value contradicts the score reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests greater than 'num_tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
