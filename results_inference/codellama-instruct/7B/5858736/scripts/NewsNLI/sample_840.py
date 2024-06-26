premise_ipads = 2
hypothesis_ipads = 2

if premise_ipads!= hypothesis_ipads:
    label = "contradiction"
else:
    label = "entailment"

print(label)
