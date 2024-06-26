purchase_quantity_premise = 20
purchase_quantity_hypothesis = 20

# the hypothesis talks about the quantity of items purchased, which is also mentioned in the premise
if purchase_quantity_hypothesis <= purchase_quantity_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif purchase_quantity_hypothesis > purchase_quantity_premise:
    # if the hypothesis value is greater than the premise value, it entails the hypothesis
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
