priya_ratio_premise = 4
mani_ratio_premise = 4
rani_ratio_premise = 8

priya_ratio_hypothesis = 2
mani_ratio_hypothesis = 4
rani_ratio_hypothesis = 8

# the hypothesis refers to the ratio of money distribution between Priya, Mani and Rani, which is also mentioned in the premise
if priya_ratio_hypothesis >= priya_ratio_premise:
    # check if the ratio of money distribution to Priya in the hypothesis contradicts the estimate of less than 'priya_ratio_premise'
    label = "contradiction"
elif mani_ratio_hypothesis!= mani_ratio_premise or rani_ratio_hypothesis!= rani_ratio_premise:
    # check if the ratio of money distribution to Mani and Rani in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of money distribution to Priya
    # any ratio less than 'priya_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
