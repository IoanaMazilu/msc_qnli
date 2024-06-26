tests_premise = 6
tests_hypothesis = 4
mean_score_premise = 50
mean_score_hypothesis = 50

# the hypothesis refers to the number of tests and the mean score, both mentioned in the premise
if tests_premise < tests_hypothesis:
    # check if the hypothesis value contradicts the number of tests in the premise
    label = "contradiction"
elif mean_score_hypothesis!= mean_score_premise:
    # check if the mean score in the hypothesis contradicts the mean score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
