priya_mani_rani_ratio_premise = 4
priya_mani_rani_ratio_hypothesis = 2

# the hypothesis refers to the ratio of money division between Priya, Mani and Rani
if priya_mani_rani_ratio_hypothesis >= priya_mani_rani_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of money division
    # any ratio less than 'priya_mani_rani_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
