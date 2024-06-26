tax_rate_premise = 28
tax_rate_hypothesis = 28

# the hypothesis and premise mention the same tax rate proposed by Obama
if tax_rate_hypothesis != tax_rate_premise:
    # check if the tax rate in the hypothesis contradicts the tax rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
