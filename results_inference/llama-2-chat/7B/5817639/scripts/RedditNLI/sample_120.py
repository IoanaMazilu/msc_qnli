base_rate_premise = 2023 # assume the base rate in the premise is 2023
base_rate_hypothesis = 2028 # assume the base rate in the hypothesis is 2028

# check if the base rate in the hypothesis contradicts the base rate in the premise
if base_rate_hypothesis!= base_rate_premise:
    label = "contradiction"
else:
    # if the base rates in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
