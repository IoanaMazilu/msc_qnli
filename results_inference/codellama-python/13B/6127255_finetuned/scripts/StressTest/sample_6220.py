ratio_priya_premise = 4
ratio_priya_hypothesis = 2
ratio_mani_premise = 4
ratio_mani_hypothesis = 4
ratio_rani_premise = 8
ratio_rani_hypothesis = 8

# the hypothesis refers to the ratio of the money division mentioned in the premise
if ratio_priya_hypothesis >= ratio_priya_premise:
    # check if the ratio of Priya's share in the hypothesis contradicts the estimate of less than 'ratio_priya_premise'
    label = "contradiction"
elif ratio_mani_hypothesis!= ratio_mani_premise or ratio_rani_hypothesis!= ratio_rani_premise:
    # check if the ratio of Mani's or Rani's share in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Priya's share
    # any ratio less than 'ratio_priya_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
