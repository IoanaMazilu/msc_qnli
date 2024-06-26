anil_son_ratio_premise = 7/3
anil_son_ratio_hypothesis = 1/3

# the hypothesis refers to the age ratio of Anil and his son mentioned in the premise
if anil_son_ratio_hypothesis!= anil_son_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
