test_num_premise = 6
test_num_hypothesis = 4
test_score_premise = 35
test_score_hypothesis = 35

# the hypothesis refers to the number of tests and the average test score mentioned in the premise
if test_num_hypothesis >= test_num_premise:
    # check if the number of tests in the hypothesis contradicts the estimate of less than 'test_num_premise'
    label = "contradiction"
elif test_score_hypothesis != test_score_premise:
    # check if the average test score in the hypothesis contradicts the average test score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
