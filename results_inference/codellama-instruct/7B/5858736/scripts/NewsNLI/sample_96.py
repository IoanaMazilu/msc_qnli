premise_percentage = 0.09
hypothesis_percentage = 0.09

if premise_percentage!= hypothesis_percentage:
    label = "contradiction"
else:
    label = "entailment"

print(label)
