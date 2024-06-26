sheep_horses_ratio_premise = 6/7
sheep_horses_ratio_hypothesis = 1/7

# the hypothesis talks about the ratio between the number of sheep and horses in the farm, which is also referenced in the premise
if sheep_horses_ratio_hypothesis >= sheep_horses_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than'sheep_horses_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of sheep to horses
    # any ratio less than'sheep_horses_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
