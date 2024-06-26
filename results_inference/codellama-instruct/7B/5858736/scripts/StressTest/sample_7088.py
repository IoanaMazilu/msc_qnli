premise_hours_worked = 6
hypothesis_hours_worked = 5

if hypothesis_hours_worked < premise_hours_worked:
    label = "entailment"
else:
    label = "contradiction"

print(label)
