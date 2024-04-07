# Premise: Jerry’s average (arithmetic mean) score on the first 3 of 4 tests is 85.
# Hypothesis: Jerry’s average (arithmetic mean) score on the first less than 3 of 4 tests is 85.
# Golden Label: contradiction

average_score_premise = 85
average_score_hypothesis = 85
test_count_premise = 3
test_count_hypothesis = 3

# the hypothesis refers to the average score and the number of tests mentioned in the premise
if average_score_premise != average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
elif test_count_hypothesis >= test_count_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

