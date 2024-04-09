share_difference_premise = 200
share_difference_hypothesis = 200

# the hypothesis refers to the difference between Mani and Rani's share mentioned in the premise
if share_difference_hypothesis <= share_difference_premise:
    # check if the hypothesis value contradicts the estimate of more than'share_difference_hypothesis'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference between shares
    # any difference greater than'share_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
