premise_num = 500000
hypothesis_num = 500000

if premise_num!= hypothesis_num:
    label = "contradiction"
else:
    label = "entailment"

print(label)
