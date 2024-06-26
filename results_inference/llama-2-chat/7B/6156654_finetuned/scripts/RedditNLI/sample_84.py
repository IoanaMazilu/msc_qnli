# The premise and hypothesis are both related to the unemployment rate and job growth in the US

# The premise states the unemployment rate fell to 3.9%
# The hypothesis states the unemployment rate will fall to 3.9%
if premise.unemployment_rate!= hypothesis.unemployment_rate:
    # If the unemployment rate in the premise and hypothesis are different, it's a contradiction
    label = "contradiction"
else:
    # If the unemployment rate in the premise and hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)
