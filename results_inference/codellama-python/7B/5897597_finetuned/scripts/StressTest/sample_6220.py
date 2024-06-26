priya_ratio_premise = 4
mani_ratio_premise = 4
rani_ratio_premise = 8

priya_ratio_hypothesis = 2
mani_ratio_hypothesis = 4
rani_ratio_hypothesis = 8

# the hypothesis refers to the ratio of money distribution between Priya, Mani and Rani mentioned in the premise
if priya_ratio_hypothesis >= priya_ratio_premise:
    # check if the ratio of Priya's share in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif mani_ratio_hypothesis!= mani_ratio_premise:
    # check if the ratio of Mani's share in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif rani_ratio_hypothesis!= rani_ratio_premise:
    # check if the ratio of Rani's share in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Priya's share
    # any ratio less than 'priya_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
