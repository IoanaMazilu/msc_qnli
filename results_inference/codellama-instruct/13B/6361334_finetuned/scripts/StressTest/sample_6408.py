offer_premise = 20
offer_hypothesis = 80

# the hypothesis refers to the percentage of discount offered by the shop, which is also mentioned in the premise
if offer_hypothesis >= offer_premise:
    # check if the hypothesis value contradicts the percentage of discount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of discount
    # any percentage of discount less than 'offer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
