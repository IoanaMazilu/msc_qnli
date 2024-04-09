offer_premise = 80
offer_hypothesis = 20

# the hypothesis talks about the offer given by the shop, which is also mentioned in the premise
if offer_hypothesis <= offer_premise:
    # check if the hypothesis value contradicts the estimate of less than 'offer_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the offer,
    # any offer greater than 'offer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
