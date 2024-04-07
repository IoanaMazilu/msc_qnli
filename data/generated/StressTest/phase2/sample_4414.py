# Premise: Jerry’s average (arithmetic mean) score on the first less than 8 of 4 tests is 85.
# Hypothesis: Jerry’s average (arithmetic mean) score on the first 3 of 4 tests is 85.
# Golden Label: neutral

tests_premise = 8
tests_hypothesis = 3
average_score_premise = 85
average_score_hypothesis = 85

# the hypothesis refers to the number of tests and average score mentioned in the premise
if tests_premise < tests_hypothesis:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
elif average_score_hypothesis != average_score_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
