# The hypothesis value is greater than the premise value
hypothesis_value = 50000
premise_value = 10000

# the hypothesis is consistent with the premise
if hypothesis_value <= premise_value:
    label = "contradiction"
else:
    label = "entailment"

print(label)
