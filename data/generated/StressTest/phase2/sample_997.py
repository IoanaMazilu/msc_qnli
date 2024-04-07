# Premise: Nick's average (arithmetic mean) test score on less than 7 tests is 78.
# Hypothesis: Nick's average (arithmetic mean) test score on 4 tests is 78.
# Golden Label: neutral

test_count_premise = 7
test_count_hypothesis = 4
average_score_premise = 78
average_score_hypothesis = 78

# the hypothesis refers to the number of tests and the average score mentioned in the premise
if test_count_hypothesis >= test_count_premise:
    # check if the number of tests in the hypothesis contradicts the premise
    label = "contradiction"
elif average_score_hypothesis != average_score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

