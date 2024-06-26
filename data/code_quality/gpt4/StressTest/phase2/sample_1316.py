store_z_price_premise = 90
store_z_price_hypothesis = 20

# The hypothesis also talks about the price of items at Store Z
if store_z_price_premise != store_z_price_hypothesis:
    # check if the price mentioned in the hypothesis contradicts the price mentioned in the premise
    label = "contradiction"
else:
    # if the price in the hypothesis does not contradict the price in the premise, we can infer entailment
    label = "entailment"

print(label)
