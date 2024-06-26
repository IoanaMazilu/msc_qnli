premise_dimensions = 3 * 5 * 5
hypothesis_dimensions = 5 * 5 * 5

if premise_dimensions <= hypothesis_dimensions:
    label = "contradiction"
elif hypothesis_dimensions!= 1 * 1 * 1:
    label = "contradiction"
else:
    label = "entailment"

print(label)
