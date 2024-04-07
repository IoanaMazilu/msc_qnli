# Premise: Jerry’s average (arithmetic mean) score on the first 3 of 4 tests is 81.
# Hypothesis: Jerry’s average (arithmetic mean) score on the first less than 3 of 4 tests is 81.
# Golden Label: contradiction

average_score_premise = 81
average_score_hypothesis = 81
tests_premise = 3
tests_hypothesis = 3

# the hypothesis refers to the average score and the number of tests mentioned in the premise
if average_score_premise != average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
elif tests_hypothesis >= tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

