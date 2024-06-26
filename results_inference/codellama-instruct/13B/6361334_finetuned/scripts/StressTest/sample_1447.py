deaths_premise = 4
deaths_hypothesis = 5
fleeing_premise = 15
fleeing_hypothesis = 15

# the hypothesis refers to the number of deaths and fleeing people mentioned in the premise
if deaths_premise <= deaths_hypothesis:
    # check if the estimate of 'deaths_hypothesis' contradicts the number of deaths in the premise
    label = "contradiction"
elif fleeing_hypothesis!= fleeing_premise:
    # check if the number of fleeing people in the hypothesis contradicts the number of fleeing people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
