premise_oil_leaked = 6522.0 - 5165.0
hypothesis_oil_leaked = 1357.0

# the hypothesis refers to the amount of oil leaked, which is also mentioned in the premise
# check if the amount of oil leaked from the hypothesis contradicts the amount of oil leaked from the premise
if hypothesis_oil_leaked!= premise_oil_leaked:
    label = "contradiction"
else:
    label = "entailment"

print(label)
