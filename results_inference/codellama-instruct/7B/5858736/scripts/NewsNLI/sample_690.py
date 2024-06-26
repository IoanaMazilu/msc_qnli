premise_lead = 5
hypothesis_lead = 5

if hypothesis_lead!= premise_lead:
    label = "contradiction"
else:
    label = "entailment"

print(label)
