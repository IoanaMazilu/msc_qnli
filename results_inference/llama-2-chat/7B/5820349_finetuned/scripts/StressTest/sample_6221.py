priya_ratio_premise = 2
mani_ratio_premise = 4
rani_ratio_premise = 8

priya_ratio_hypothesis = 2
mani_ratio_hypothesis = 4
rani_ratio_hypothesis = 8

# the hypothesis refers to the ratio of money division between Priya, Mani and Rani mentioned in the premise
if priya_ratio_hypothesis >= priya_ratio_premise:
    # check if the ratio of 'priya_ratio_hypothesis' contradicts the ratio of Priya's share in the premise
    label = "contradiction"
elif mani_ratio_hypothesis!= mani_ratio_premise or rani_ratio_hypothesis!= rani_ratio_premise:
    # check if the ratio of Mani's or Rani's share in the hypothesis contradicts the ratio of their shares in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)