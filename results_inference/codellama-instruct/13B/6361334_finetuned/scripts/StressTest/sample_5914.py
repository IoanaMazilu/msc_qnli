tests_premise = 4
tests_hypothesis = 3
score_premise = 90
score_hypothesis = 90

# the hypothesis refers to the number of tests and the score mentioned in the premise
if tests_hypothesis <= tests_premise:
    # check if the hypothesis value contradicts the number of tests in the premise
    label = "contradiction"
elif score_hypothesis!= score_premise:
    # check if the score in the hypothesis contradicts the score mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
