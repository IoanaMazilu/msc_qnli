premise_length = 180
hypothesis_length = 180

if hypothesis_length!= premise_length:
    label = "contradiction"
else:
    label = "entailment"

print(label)
