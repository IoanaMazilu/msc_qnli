tests_premise = 4
tests_hypothesis = 4

# the hypothesis refers to the number of tests mentioned in the premise
if tests_hypothesis > tests_premise:
    # check if the number of tests in the hypothesis contradicts the number of tests in the premise
    label = "contradiction"
elif (tests_hypothesis == tests_premise) and (arithmetic_mean_score_hypothesis!= arithmetic_mean_score_premise):
    # check if the arithmetic mean score in the hypothesis contradicts the arithmetic mean score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
