ratio_priya_premise = 2
ratio_priya_hypothesis = 2
ratio_mani_premise = 4
ratio_mani_hypothesis = 4
ratio_rani_premise = 8
ratio_rani_hypothesis = 8

# the hypothesis refers to the ratio of money distribution between Priya, Mani and Rani mentioned in the premise
if ratio_priya_hypothesis >= ratio_priya_premise:
    # check if the ratio of Priya's share in the hypothesis contradicts the ratio of Priya's share in the premise
    label = "contradiction"
elif ratio_mani_hypothesis!= ratio_mani_premise:
    # check if the ratio of Mani's share in the hypothesis contradicts the ratio of Mani's share in the premise
    label = "contradiction"
elif ratio_rani_hypothesis!= ratio_rani_premise:
    # check if the ratio of Rani's share in the hypothesis contradicts the ratio of Rani's share in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
