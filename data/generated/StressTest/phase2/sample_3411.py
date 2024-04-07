# Premise: Joe’s average (arithmetic mean) test score across 4 equally weighted tests was 60.
# Hypothesis: Joe’s average (arithmetic mean) test score across less than 6 equally weighted tests was 60.
# Golden Label: entailment

test_count_premise = 4
test_count_hypothesis = 6
average_score_premise = 60
average_score_hypothesis = 60

# the hypothesis refers to Joe's average test score mentioned in the premise, but with different test counts
if average_score_hypothesis != average_score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
elif test_count_hypothesis <= test_count_premise:
    # check if the test count in the hypothesis contradicts the test count in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

