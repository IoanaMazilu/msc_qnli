# Premise: Robin's average (arithmetic mean) test score on more than 2 tests is 82.
# Hypothesis: Robin's average (arithmetic mean) test score on 9 tests is 82.
# Golden Label: neutral

average_score_premise = 82
average_score_hypothesis = 82
tests_premise = 2
tests_hypothesis = 9

# the hypothesis refers to the average test score and number of tests taken by Robin, mentioned in the premise as well
if average_score_hypothesis != average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif tests_hypothesis <= tests_premise:
    # check if the number of tests in the hypothesis contradicts the 'more than' figure in the premise
    label = "contradiction"
else:
    # the premise gives only a lower limit for the number of tests
    # any number of tests greater than 'tests_premise' with the same average score is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

