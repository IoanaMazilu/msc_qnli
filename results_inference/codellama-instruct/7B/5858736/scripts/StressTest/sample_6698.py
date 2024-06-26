premise_amount = 2000
hypothesis_amount = 7000

if hypothesis_amount <= premise_amount:
    label = "contradiction"
else:
    label = "neutral"

print(label)
