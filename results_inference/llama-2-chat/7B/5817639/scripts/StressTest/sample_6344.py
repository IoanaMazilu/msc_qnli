discount_premise = 288
discount_hypothesis = 888

# the hypothesis talks about a larger discount value and the same time period as the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the estimate of the discount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any larger discount value than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
