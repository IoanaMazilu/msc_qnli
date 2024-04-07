# Premise: Shop Offered 20% offer for every Shirt, Smith bought a shirt at Rs.
# Hypothesis: Shop Offered less than 80% offer for every Shirt, Smith bought a shirt at Rs.
# Golden Label: entailment

offer_premise = 20
offer_hypothesis = 80

# the hypothesis refers to the discount percentage offered by the shop mentioned in the premise
if offer_hypothesis <= offer_premise:
    # check if the offer percentage in the hypothesis contradicts the offer percentage in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

