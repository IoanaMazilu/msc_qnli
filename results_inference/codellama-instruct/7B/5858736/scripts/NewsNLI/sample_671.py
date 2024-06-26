premise_inmates = 200
hypothesis_inmates = 200

if hypothesis_inmates!= premise_inmates:
    label = "contradiction"
else:
    label = "entailment"

print(label)
