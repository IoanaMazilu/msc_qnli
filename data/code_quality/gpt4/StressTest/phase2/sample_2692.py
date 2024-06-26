test_count_premise = 5
test_count_hypothesis = 4
average_score_premise = 40
average_score_hypothesis = 40

# the hypothesis refers to Joe's average test score, number of tests, and weight of tests mentioned in the premise
if test_count_hypothesis >= test_count_premise:
    # check if the number of tests in the hypothesis contradicts the premise
    label = "contradiction"
elif average_score_hypothesis != average_score_premise:
    # check if the average test score in the hypothesis contradicts the average test score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
