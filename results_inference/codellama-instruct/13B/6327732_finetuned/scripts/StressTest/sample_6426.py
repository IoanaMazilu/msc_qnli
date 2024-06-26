premise_value = 450
hypothesis_value = 750

# the hypothesis refers to the value of the item sold and the premise mentions the value of the item sold
if hypothesis_value <= premise_value:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the value of the item sold
    # any value greater than 'premise_value' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
