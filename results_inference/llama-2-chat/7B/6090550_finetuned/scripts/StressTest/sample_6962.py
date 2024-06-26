tests_premise = 4
tests_hypothesis = 4
score_premise = 60
score_hypothesis = 60

# the hypothesis talks about the average test score of Joe across more than 4 equally weighted tests
if tests_hypothesis <= tests_premise:
    # check if the hypothesis value contradicts the premise of more than 'tests_premise' tests
    label = "contradiction"
else:
    # the premise gives the exact number of tests
    # any number of tests greater than 'tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
