grape_purchase_premise = 7 * 68 = 466
mango_purchase_premise = 9 * 48 = 432

grape_purchase_hypothesis = less_than_7 * 68
mango_purchase_hypothesis = 9 * 48

# check if the hypothesis values contradict the premise ones
if grape_purchase_hypothesis < grape_purchase_premise and mango_purchase_hypothesis == mango_purchase_premise:
    label = "contradiction"
elif grape_purchase_hypothesis > grape_purchase_premise:
    # the hypothesis refers to a lesser amount of grapes, which is consistent with the premise
    label = "neutral"
else:
    # the hypothesis refers to the same amount of mangoes, which is consistent with the premise
    label = "neutral"

print(label)
