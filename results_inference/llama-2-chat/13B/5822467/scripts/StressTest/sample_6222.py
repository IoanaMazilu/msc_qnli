mani_share_premise = 200
rani_share_premise = 200
difference_premise = mani_share_premise - rani_share_premise

# the hypothesis refers to the difference between Mani and Rani's share
hypothesis_difference = less_than_400

# check if the hypothesis value contradicts the estimate of the difference in the premise
if hypothesis_difference > difference_premise:
    label = "contradiction"
elif hypothesis_difference <= difference_premise:
    # the hypothesis value is consistent with the estimate of the difference in the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the difference
    # any difference less than 400 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
