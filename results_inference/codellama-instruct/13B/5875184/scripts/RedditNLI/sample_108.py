premise_payrolls = 164000
premise_jobless_rate = 3.9

hypothesis_payrolls = 164000
hypothesis_jobless_rate = 3.9

if premise_payrolls!= hypothesis_payrolls:
    label = "contradiction"
elif premise_jobless_rate!= hypothesis_jobless_rate:
    label = "contradiction"
else:
    label = "entailment"

print(label)
