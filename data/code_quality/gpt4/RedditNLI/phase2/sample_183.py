tax_increase_premise = 522
tax_increase_hypothesis = 522

# the hypothesis and premise mention the tax increase on China steel by the US
if tax_increase_hypothesis != tax_increase_premise:
    # check if the tax increase in the hypothesis contradicts the tax increase in the premise
    label = "contradiction"
else:
    # if the tax increase in the hypothesis does not contradict the tax increase in the premise, we can infer entailment
    label = "entailment"

print(label)
