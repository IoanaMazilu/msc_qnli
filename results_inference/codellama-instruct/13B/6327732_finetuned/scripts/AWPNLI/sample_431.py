premise_oil_leaked = 6522.0 - 5165.0
hypothesis_oil_leaked = 1358.0

if premise_oil_leaked!= hypothesis_oil_leaked:
    label = "contradiction"
else:
    label = "entailment"

print(label)
