# Premise: Shop Offered less than 52% offer for every Shirt, Smith bought a shirt at Rs.
# Hypothesis: Shop Offered 32% offer for every Shirt, Smith bought a shirt at Rs.
# Golden Label: neutral

offer_premise = 52
offer_hypothesis = 32

# the hypothesis talks about the discount offered on a shirt, referenced also in the premise
if offer_hypothesis >= offer_premise:
    # check if the hypothesis value contradicts the estimate of less than 'offer_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount less than 'offer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

