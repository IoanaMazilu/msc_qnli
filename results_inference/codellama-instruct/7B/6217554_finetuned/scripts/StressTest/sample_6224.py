difference_share_premise = 200
difference_share_hypothesis = 200

# the hypothesis gives an estimate for the difference between Mani and Rani's share
if difference_share_hypothesis <= difference_share_premise:
    # check if the hypothesis value contradicts the estimate of more than 'difference_share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference between Mani and Rani's share
    # any number of difference greater than 'difference_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
