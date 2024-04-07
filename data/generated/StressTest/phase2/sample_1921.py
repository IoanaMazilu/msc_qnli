# Premise: Shop Offered less than 45% offer for every Shirt, Smith bought a shirt at Rs.
# Hypothesis: Shop Offered 25% offer for every Shirt, Smith bought a shirt at Rs.
# Golden Label: neutral

offer_premise = 45
offer_hypothesis = 25

# the hypothesis talks about the offer percentage on a shirt, referenced also in the premise
if offer_hypothesis >= offer_premise:
    # check if the hypothesis value contradicts the estimate of less than 'offer_premise'
    label = "contradiction"
elif offer_hypothesis < offer_premise:
    # the premise gives only an estimate for the offer percentage 
    # any offer percentage less than 'offer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

