sheep_horse_ratio_premise = 3 / 7
sheep_horse_ratio_hypothesis = 4 / 7

# the hypothesis refers to the ratio between the number of sheep and the number of horses at the Stewart farm, also mentioned in the premise
if sheep_horse_ratio_hypothesis <= sheep_horse_ratio_premise:
    # check if the ratio provided in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio is more than the premise ratio, 
    # it does not contradict the premise, but also cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
