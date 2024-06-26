tax_cut_premise = 300 * 10**9  # 300 billion
tax_cut_hypothesis = 300 * 10**9  # 300 billion

# the hypothesis and premise mention the same tax cut amount associated with Obama
if tax_cut_premise != tax_cut_hypothesis:
    # check if the tax cut amount in the hypothesis contradicts the tax cut amount in the premise
    label = "contradiction"
else:
    # if the tax cut amount in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
