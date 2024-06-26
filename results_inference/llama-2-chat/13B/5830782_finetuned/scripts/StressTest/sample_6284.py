test_score_premise = 82
test_score_hypothesis = 82
tests_taken_premise = 9
tests_taken_hypothesis = 9

# the hypothesis refers to Robin's average test score and number of tests taken mentioned in the premise
if test_score_hypothesis!= test_score_premise:
    # check if the average test score in the hypothesis contradicts the average test score reported in the premise
    label = "contradiction"
elif tests_taken_hypothesis <= tests_taken_premise:
    # check if the number of tests taken in the hypothesis contradicts the number of tests taken reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
