# Premise: Shop Offered more than 30% offer for every Shirt, Smith bought a shirt at Rs.
# Hypothesis: Shop Offered 40% offer for every Shirt, Smith bought a shirt at Rs.
# Golden Label: neutral

offer_premise = 30
offer_hypothesis = 40

# the hypothesis talks about the discount offered for a shirt, which is also mentioned in the premise
if offer_hypothesis <= offer_premise:
    # check if the hypothesis value contradicts the estimate of more than 'offer_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the offer
    # any percentage of offer greater than 'offer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

