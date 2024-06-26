priya_mani_rani_ratio_premise = (4, 4, 8)
priya_mani_rani_ratio_hypothesis = (2, 4, 8)

# the hypothesis refers to the ratio of money division between Priya, Mani and Rani mentioned in the premise
if priya_mani_rani_ratio_hypothesis!= priya_mani_rani_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
