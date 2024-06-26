priya_mani_rani_premise = 2/4/8
priya_mani_rani_hypothesis = 2/4/8

# the hypothesis refers to the ratio of money distribution between Priya, Mani and Rani mentioned in the premise
if priya_mani_rani_hypothesis >= priya_mani_rani_premise:
    # check if the estimate of 'priya_mani_rani_hypothesis' contradicts the ratio of money distribution in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the ratio of money distribution
    # any ratio less than 'priya_mani_rani_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
