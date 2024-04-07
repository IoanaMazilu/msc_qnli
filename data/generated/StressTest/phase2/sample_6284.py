# Premise: Robin's average (arithmetic mean) test score on 9 tests is 82.
# Hypothesis: Robin's average (arithmetic mean) test score on more than 9 tests is 82.
# Golden Label: contradiction

tests_premise = 9
tests_hypothesis = 9
average_score_premise = 82
average_score_hypothesis = 82

# the hypothesis refers to the number of tests and average score mentioned in the premise
if tests_hypothesis <= tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests mentioned in the premise
    label = "contradiction"
elif average_score_hypothesis != average_score_premise:
    # check if the average score in the hypothesis contradicts the average score mentioned in the premise
    label = "contradiction"
else:
    # any number of tests more than 'tests_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

