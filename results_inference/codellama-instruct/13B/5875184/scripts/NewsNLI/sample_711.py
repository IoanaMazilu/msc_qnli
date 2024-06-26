premise_amount = 45000
hypothesis_amount = 45000

if hypothesis_amount > premise_amount:
    label = "entailment"
elif hypothesis_amount < premise_amount:
    label = "contradiction"
else:
    label = "neutral"

print(label)
