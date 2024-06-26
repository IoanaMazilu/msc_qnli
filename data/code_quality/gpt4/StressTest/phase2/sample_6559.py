average_score_premise = 78
average_score_hypothesis = 78
tests_premise = 6
tests_hypothesis = 3

# the hypothesis refers to the average score and the number of tests taken by Jerry, which are also mentioned in the premise
if average_score_hypothesis != average_score_premise:
    # check if the average score in the hypothesis contradicts the average score given in the premise
    label = "contradiction"
elif tests_hypothesis > tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
