# Premise: Shop Offered 32% offer for every Shirt, Smith bought a shirt at Rs.
# Hypothesis: Shop Offered less than 32% offer for every Shirt, Smith bought a shirt at Rs.
# Golden Label: contradiction

offer_percentage_premise = 32
offer_percentage_hypothesis = 32

# the hypothesis refers to the discount offered on shirts which is also mentioned in the premise
if offer_percentage_hypothesis < offer_percentage_premise:
    # check if the discount in the hypothesis is less than the discount given in the premise
    label = "contradiction"
elif offer_percentage_hypothesis > offer_percentage_premise:
    # check if the discount in the hypothesis is more than the discount given in the premise
    label = "contradiction"
else:
    # if the discount percentage in the hypothesis is equal to the discount percentage in the premise, we can infer entailment
    label = "entailment"

print(label)

