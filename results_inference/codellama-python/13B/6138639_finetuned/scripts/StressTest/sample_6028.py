average_score_premise = 50
tests_premise = 6
tests_hypothesis = 4

# the hypothesis talks about the average score and number of tests, referenced also in the premise
if tests_hypothesis >= tests_premise:
    # check if the number of tests in the hypothesis contradicts the estimate of less than 'tests_premise'
    label = "contradiction"
elif average_score_premise!= 50:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests less than 'tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)