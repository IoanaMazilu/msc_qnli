purchase_price_premise = 9/10
purchase_price_hypothesis = 5/10
sale_percentage_premise = 8
sale_percentage_hypothesis = 8

# the hypothesis refers to the purchase and selling prices of the pressure cooker mentioned in the premise
if purchase_price_premise <= purchase_price_hypothesis:
    # check if the estimate of 'purchase_price_hypothesis' contradicts the purchase price in the premise
    label = "contradiction"
elif sale_percentage_hypothesis != sale_percentage_premise:
    # check if the selling percentage in the hypothesis contradicts the selling percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
