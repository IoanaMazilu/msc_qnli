# Premise: Ravi's average (arithmetic mean) test score on less than 5 tests is 78.
# Hypothesis: Ravi's average (arithmetic mean) test score on 4 tests is 78.
# Golden Label: neutral

tests_premise = 5
tests_hypothesis = 4
score_premise = 78
score_hypothesis = 78

# the hypothesis refers to the number of tests and the average score mentioned in the premise
if tests_hypothesis >= tests_premise:
    # check if the number of tests in the hypothesis contradicts the 'less than' condition for the number of tests in the premise
    label = "contradiction"
elif score_hypothesis != score_premise:
    # check if the average score in the hypothesis contradicts the average score mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and conditions do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

