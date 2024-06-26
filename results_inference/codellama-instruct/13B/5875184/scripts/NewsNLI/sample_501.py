premise_cartons = 2498
hypothesis_bacteria = 13

if premise_cartons!= hypothesis_bacteria:
    label = "contradiction"
else:
    label = "entailment"

print(label)
