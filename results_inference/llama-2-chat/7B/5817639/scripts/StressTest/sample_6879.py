purchase_value_premise = 1500
purchase_value_hypothesis = 6500

# the hypothesis refers to the amount of money spent on US saving bonds, which is also mentioned in the premise
if purchase_value_hypothesis <= purchase_value_premise:
    # check if the hypothesis value contradicts the estimate of 'purchase_value_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the amount of money spent, and the hypothesis provides a lower value, which is consistent with the premise
    label = "entailment"

print(label)
