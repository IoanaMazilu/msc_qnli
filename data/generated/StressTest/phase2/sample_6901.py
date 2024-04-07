# Premise: Shop Offered less than 70% offer for every Shirt, Smith bought a shirt at Rs.
# Hypothesis: Shop Offered 30% offer for every Shirt, Smith bought a shirt at Rs.
# Golden Label: neutral

offer_premise = 70
offer_hypothesis = 30

# the hypothesis talks about the percentage of discount for a shirt, referenced also in the premise
if offer_hypothesis >= offer_premise:
    # check if the hypothesis value contradicts the estimate of less than 'offer_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of discount
    # any percentage of discount less than 'offer_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

