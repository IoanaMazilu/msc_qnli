premise_amount = 85
hypothesis_amount = 95

if hypothesis_amount <= premise_amount:
    label = "contradiction"
else:
    label = "entailment"

print(label)
