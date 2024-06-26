store_z_price_premise = 90
store_z_price_hypothesis = 90

# the hypothesis implies that the price at Store Z is less than what is stated in the premise
if store_z_price_hypothesis < store_z_price_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
elif store_z_price_hypothesis > store_z_price_premise:
    # check if the estimated price in the hypothesis is greater than the price in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
