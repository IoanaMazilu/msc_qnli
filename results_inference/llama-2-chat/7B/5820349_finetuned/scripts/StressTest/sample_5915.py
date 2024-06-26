tests_premise = 3
tests_hypothesis = 3
score_average_premise = 90
score_average_hypothesis = 90

# the hypothesis refers to the average score on the first 'tests_hypothesis' tests mentioned in the premise
if tests_hypothesis <= tests_premise:
    # check if the hypothesis value contradicts the number of tests in the premise
    label = "contradiction"
elif score_average_hypothesis!= score_average_premise:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
