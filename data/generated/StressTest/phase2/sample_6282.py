# Premise: Robin's average (arithmetic mean) test score on 9 tests is 82.
# Hypothesis: Robin's average (arithmetic mean) test score on more than 2 tests is 82.
# Golden Label: entailment

tests_taken_premise = 9
tests_taken_hypothesis = 2
average_score_premise = 82
average_score_hypothesis = 82

# the hypothesis refers to Robin's average test score and the number of tests taken, which are also mentioned in the premise
if average_score_premise != average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif tests_taken_hypothesis >= tests_taken_premise:
    # check if the number of tests taken in the hypothesis contradicts the number of tests taken reported in the premise
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

