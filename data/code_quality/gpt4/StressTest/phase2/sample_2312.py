store_Z_price_premise = 90
store_Z_price_hypothesis = 20

# the hypothesis refers to the price in Store Z mentioned in the premise
if store_Z_price_premise != store_Z_price_hypothesis:
    # check if the price in Store Z in the hypothesis contradicts the price in Store Z reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
