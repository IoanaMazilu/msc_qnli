quantity_premise = 20
quantity_hypothesis = 20

# the hypothesis refers to the quantity of items purchased from Ram by Mohan, mentioned in the premise
if quantity_hypothesis <= quantity_premise:
    # check if the estimate of 'quantity_hypothesis' contradicts the quantity mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity
    # any quantity greater than 'quantity_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
