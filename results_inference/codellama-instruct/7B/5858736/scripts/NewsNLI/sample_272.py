premise_bail = 1000000
hypothesis_bail = 1000000

if premise_bail!= hypothesis_bail:
    label = "contradiction"
else:
    label = "entailment"

print(label)
