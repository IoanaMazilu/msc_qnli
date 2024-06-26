dead_women_premise = 17
dead_children_premise = 6
dead_women_hypothesis = 17
dead_children_hypothesis = 6

# the hypothesis mentions the number of women and children among the dead, which is also mentioned in the premise
if dead_women_hypothesis!= dead_women_premise:
    # check if the number of dead women in the hypothesis contradicts the number of dead women reported in the premise
    label = "contradiction"
elif dead_children_hypothesis!= dead_children_premise:
    # check if the number of dead children from the hypothesis contradicts the number of dead children in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
