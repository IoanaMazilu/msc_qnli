test_number_premise = 6
test_number_hypothesis = 4
score_premise = 60
score_hypothesis = 60

# the hypothesis refers to the number of tests and the average score mentioned in the premise
if test_number_hypothesis >= test_number_premise:
    # check if the number of tests in the hypothesis contradicts the premise statement of less than 'test_number_premise' tests
    label = "contradiction"
elif score_hypothesis != score_premise:
    # check if the average test score in the hypothesis contradicts the average test score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
