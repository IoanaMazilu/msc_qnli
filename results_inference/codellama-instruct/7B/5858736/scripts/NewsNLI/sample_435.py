premise_restitution = 860000
hypothesis_restitution = 860000

if premise_restitution!= hypothesis_restitution:
    label = "contradiction"
else:
    label = "entailment"

print(label)
