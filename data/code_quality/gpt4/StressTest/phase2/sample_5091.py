tests_premise = 3
tests_hypothesis = 5
score_average_premise = 85
score_average_hypothesis = 85

# the hypothesis refers to the same tests and their average score mentioned in the premise
if tests_hypothesis <= tests_premise and score_average_hypothesis == score_average_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
elif score_average_hypothesis != score_average_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
