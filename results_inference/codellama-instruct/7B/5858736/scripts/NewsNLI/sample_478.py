premise_helicopters = 2
hypothesis_helicopters = 2

if premise_helicopters!= hypothesis_helicopters:
    label = "contradiction"
else:
    label = "entailment"

print(label)
