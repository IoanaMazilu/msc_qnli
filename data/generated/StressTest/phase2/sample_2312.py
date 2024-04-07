# Premise: Store Z:$90, a 10% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Hypothesis: Store Z:$20, a 10% sales tax, and $10 rebate after tax Isaac can purchase a certain item in four different ways, as shown in the table.
# Golden Label: contradiction

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

