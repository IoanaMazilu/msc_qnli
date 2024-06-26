premise_value = 500000000
hypothesis_value = 100000000

if hypothesis_value!= premise_value:
    label = "contradiction"
else:
    label = "entailment"

print(label)
