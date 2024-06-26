average_score_premise = 82
tests_premise = 9
average_score_hypothesis = 82
tests_hypothesis = 9

# the hypothesis refers to the average test score and number of tests mentioned in the premise
if average_score_premise!= average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif tests_hypothesis <= tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests
    # any number of tests greater than 'tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
