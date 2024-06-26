offer_premise = 80
offer_hypothesis = 20

# the hypothesis refers to the offer percentage for shirts mentioned in the premise
if offer_hypothesis >= offer_premise:
    # check if the offer percentage in the hypothesis contradicts the estimate of less than 'offer_premise'
    label = "contradiction"
else:
    # any offer percentage less than 'offer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
