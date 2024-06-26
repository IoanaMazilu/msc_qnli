people_dead_premise = 3
people_dead_hypothesis = 3
people_injured_premise = 52
people_injured_hypothesis = 52

# the hypothesis mentions the number of people dead and injured, which are also mentioned in the premise
if people_dead_hypothesis!= people_dead_premise:
    # check if the number of people dead in the hypothesis contradicts the number of people dead in the premise
    label = "contradiction"
elif people_injured_hypothesis!= people_injured_premise:
    # check if the number of people injured in the hypothesis contradicts the number of people injured in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
