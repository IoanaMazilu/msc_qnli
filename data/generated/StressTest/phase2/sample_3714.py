# Premise: Shop Offered 20% offer for every Shirt, Smith bought a shirt at Rs.
# Hypothesis: Shop Offered less than 50% offer for every Shirt, Smith bought a shirt at Rs.
# Golden Label: entailment

offer_percentage_premise = 20
offer_percentage_hypothesis = 50

# The hypothesis refers to the discount offer in the premise
if offer_percentage_hypothesis <= offer_percentage_premise:
    # Check if the discount offer percentage in the hypothesis contradicts the offer percentage in the premise
    label = "contradiction"
else:
    # If the discount offer percentage in the hypothesis does not contradict the discount offer percentage in the premise, we can infer entailment
    label = "entailment"

print(label)

