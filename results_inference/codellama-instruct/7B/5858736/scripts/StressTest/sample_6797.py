premise_amount = 62500
hypothesis_amount = 62500

if hypothesis_amount < premise_amount:
    label = "contradiction"
else:
    label = "neutral"

print(label)
