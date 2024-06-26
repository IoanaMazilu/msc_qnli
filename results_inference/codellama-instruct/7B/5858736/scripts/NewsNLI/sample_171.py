premise_amount = 3000000000
hypothesis_amount = 3000000000

if premise_amount!= hypothesis_amount:
    label = "contradiction"
else:
    label = "entailment"

print(label)
