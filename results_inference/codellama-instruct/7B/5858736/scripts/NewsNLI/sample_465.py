premise_amount = 10000
hypothesis_amount = 29000000

if hypothesis_amount > premise_amount:
    label = "entailment"
else:
    label = "contradiction"

print(label)
