# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 70.
# Hypothesis: Joe’s average (arithmetic mean) test score across less than 4 equally weighted tests was 70.
# Golden Label: contradiction

test_score_premise = 70
test_count_premise = 4
test_score_hypothesis = 70
test_count_hypothesis = 4

# The hypothesis refers to Joe's average test score and number of tests mentioned in the premise
if test_score_premise != test_score_hypothesis:
    # Check if the average test score referred in the hypothesis contradicts the average test score mentioned in the premise
    label = "contradiction"
elif test_count_hypothesis >= test_count_premise:
    # Check if the number of tests referred in the hypothesis contradicts the number of tests mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

