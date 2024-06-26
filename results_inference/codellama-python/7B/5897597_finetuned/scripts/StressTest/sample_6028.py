average_score_premise = 50
average_score_hypothesis = 50
tests_premise = 6
tests_hypothesis = 4

# the hypothesis talks about Joe's average test score and the number of tests, referenced also in the premise
if average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif tests_hypothesis >= tests_premise:
    # check if the number of tests in the hypothesis contradicts the estimate of less than 'tests_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests less than 'tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)