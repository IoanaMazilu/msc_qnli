grape_purchase_premise = 7 * 68 = 466
mango_purchase_premise = 9 * 48 = 432

grape_purchase_hypothesis = 1 + 466
mango_purchase_hypothesis = 9 + 432

# check if the hypothesis values contradict the premise values
if grape_purchase_hypothesis <= grape_purchase_premise and mango_purchase_hypothesis <= mango_purchase_premise:
    label = "contradiction"
elif grape_purchase_hypothesis > grape_purchase_premise or mango_purchase_hypothesis > mango_purchase_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
