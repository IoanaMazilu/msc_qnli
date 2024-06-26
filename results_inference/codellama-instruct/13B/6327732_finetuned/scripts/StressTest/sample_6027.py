tests_premise = 4
tests_hypothesis = 6
score_premise = 50
score_hypothesis = 50

# the hypothesis refers to the number of tests and the score, both mentioned in the premise
if tests_premise <= tests_hypothesis:
    # check if the hypothesis value contradicts the number of tests in the premise
    label = "contradiction"
elif score_hypothesis!= score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
