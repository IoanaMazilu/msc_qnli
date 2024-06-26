premise_value = 4610000000
hypothesis_value = 7010000000

if premise_value < hypothesis_value:
    label = "entailment"
elif premise_value > hypothesis_value:
    label = "contradiction"
else:
    label = "neutral"

print(label)
