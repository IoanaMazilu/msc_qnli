# Premise: Shop Offered 40% offer for every Shirt, Smith bought a shirt at Rs.
# Hypothesis: Shop Offered more than 30% offer for every Shirt, Smith bought a shirt at Rs.
# Golden Label: entailment

offer_premise = 40
offer_hypothesis = 30

# the hypothesis refers to the offer percentage on each shirt as mentioned in the premise
if offer_hypothesis >= offer_premise:
    # check if the hypothesis offer contradicts the premise offer
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise offer, we can infer entailment
    label = "entailment"

print(label)

