sheep_horses_premise = 6 / 7
sheep_horses_hypothesis = 6 / 7
sheep_horses_premise_horses = 6 / 7
sheep_horses_premise_sheep = 7 / 7
sheep_horses_hypothesis_horses = 6 / 7
sheep_horses_hypothesis_sheep = 7 / 7

# the hypothesis refers to the ratio between sheep and horses at the farm
if sheep_horses_premise!= sheep_horses_hypothesis:
    # check if the ratio of sheep to horses in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif sheep_horses_premise_horses!= sheep_horses_hypothesis_horses:
    # check if the ratio of horses in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif sheep_horses_premise_sheep!= sheep_horses_hypothesis_sheep:
    # check if the ratio of sheep in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
