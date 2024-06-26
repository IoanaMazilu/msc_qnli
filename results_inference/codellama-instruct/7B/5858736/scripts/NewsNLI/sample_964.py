premise_number = 42
hypothesis_budget = 19000000

if premise_number!= hypothesis_budget:
    label = "contradiction"
else:
    label = "entailment"

print(label)
