premise_troops = 4100
hypothesis_troops = 4100

if hypothesis_troops!= premise_troops:
    label = "contradiction"
else:
    label = "entailment"

print(label)
