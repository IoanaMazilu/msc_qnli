grapes_purchased_kg = 7
grapes_rate_per_kg = 68
mangoes_purchased_kg = 9
mangoes_rate_per_kg = 48

# The hypothesis refers to the purchase of grapes and mangoes
if grapes_purchased_kg > 1:
    # Check if the hypothesis value contradicts the premise value of 'grapes_purchased_kg'
    if grapes_purchased_kg <= 1:
        label = "entailment"
    else:
        label = "contradiction"
elif mangoes_purchased_kg > 1:
    # Check if the hypothesis value contradicts the premise value of'mangoes_purchased_kg'
    if mangoes_purchased_kg <= 1:
        label = "entailment"
    else:
        label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise values, it is neutral
    label = "neutral"

print(label)
