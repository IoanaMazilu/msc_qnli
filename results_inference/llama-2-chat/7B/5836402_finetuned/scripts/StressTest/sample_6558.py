tests_premise = 4
tests_hypothesis = 4
score_premise = 78
score_hypothesis = 78

# the hypothesis refers to the number of tests and the score mentioned in the premise
if tests_hypothesis >= tests_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif score_hypothesis!= score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
