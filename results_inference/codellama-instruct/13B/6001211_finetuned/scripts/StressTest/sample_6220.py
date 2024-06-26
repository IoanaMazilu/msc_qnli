priya_mani_rani_ratio_premise = 4/4/8
priya_mani_rani_ratio_hypothesis = 2/4/8

# the hypothesis refers to the ratio of money distribution between Priya, Mani and Rani, also mentioned in the premise
if priya_mani_rani_ratio_hypothesis >= priya_mani_rani_ratio_premise:
    # check if the ratio in the hypothesis contradicts the estimate of less than 'priya_mani_rani_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio less than 'priya_mani_rani_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
