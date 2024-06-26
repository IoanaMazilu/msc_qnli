mani_share_premise = 200
mani_share_hypothesis = 200

# the hypothesis refers to the difference between Mani and Rani's share, which is not explicitly mentioned in the premise
if mani_share_hypothesis <= mani_share_premise:
    # check if the estimate of'mani_share_hypothesis' contradicts the number of Mani's share in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference between Mani and Rani's share
    # any number greater than'mani_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
