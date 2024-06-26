priya_mani_rani_ratio_premise = [2, 4, 8]
priya_mani_rani_ratio_hypothesis = [4, 4, 8]

# the hypothesis refers to the ratio of money division between Priya, Mani and Rani mentioned in the premise
if priya_mani_rani_ratio_hypothesis[0] > priya_mani_rani_ratio_premise[0]:
    # check if the first element of the ratio in the hypothesis contradicts the first element in the premise ratio
    label = "contradiction"
elif priya_mani_rani_ratio_hypothesis[1:] != priya_mani_rani_ratio_premise[1:]:
    # check if the rest of the ratio in the hypothesis contradicts the rest of the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
