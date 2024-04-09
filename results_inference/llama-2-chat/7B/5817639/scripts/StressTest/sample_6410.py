offer_premise = 20
offer_hypothesis = 80

# the hypothesis talks about a higher offer for shirts, referenced in the premise
if offer_hypothesis <= offer_premise:
    # check if the hypothesis value contradicts the estimate of the offer in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the offer, any higher offer is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
