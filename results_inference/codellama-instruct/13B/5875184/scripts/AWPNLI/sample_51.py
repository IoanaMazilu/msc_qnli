premise_fresh_fruit = 9792.0 - 3513.0
premise_frozen_fruit = 3513.0
hypothesis_fresh_fruit = 6280.0

if premise_fresh_fruit >= hypothesis_fresh_fruit:
    label = "entailment"
else:
    label = "contradiction"

print(label)
