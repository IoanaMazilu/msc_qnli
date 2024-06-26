quantity_premise = 20
quantity_hypothesis = 60
price_premise = 0
price_hypothesis = 0

# the hypothesis talks about the quantity of items purchased from Ram by Mohan
if quantity_hypothesis >= quantity_premise:
    # check if the hypothesis value contradicts the quantity mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the quantity
    # any quantity less than 'quantity_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
