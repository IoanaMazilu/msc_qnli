shop_offer_premise = 0.8
shop_offer_hypothesis = 0.2

# the hypothesis refers to the offer percentage mentioned in the premise
if shop_offer_hypothesis >= shop_offer_premise:
    # check if the hypothesis value contradicts the estimate of less than'shop_offer_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the offer percentage
    # any offer percentage less than'shop_offer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
