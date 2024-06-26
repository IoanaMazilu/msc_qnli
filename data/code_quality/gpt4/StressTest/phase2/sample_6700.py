tony_share_premise = 6500
tony_share_hypothesis = 4500

# the hypothesis refers to the share of Tony mentioned in the premise
if tony_share_hypothesis >= tony_share_premise:
    # check if the hypothesis value contradicts the estimate of less than 'tony_share_premise'
    label = "contradiction"
else:
    # any share of Tony less than 'tony_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
