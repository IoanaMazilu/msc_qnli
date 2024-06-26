sheep_horses_ratio_premise = 1/7
sheep_horses_ratio_hypothesis = 6/7

# the hypothesis talks about the ratio between the number of sheep and the number of horses at the Stewart farm, referenced also in the premise
if sheep_horses_ratio_hypothesis <= sheep_horses_ratio_premise:
    # check if the hypothesis value contradicts the estimate of more than'sheep_horses_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio between the number of sheep and the number of horses
    # any ratio greater than'sheep_horses_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
