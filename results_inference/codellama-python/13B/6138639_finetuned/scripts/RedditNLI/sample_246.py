tax_cut_premise = 300
tax_cut_hypothesis = 300

# the hypothesis and premise mention the same tax cut amount
if tax_cut_hypothesis!= tax_cut_premise:
    # check if the tax cut amount in the hypothesis contradicts the tax cut amount in the premise
    label = "contradiction"
else:
    # if the tax cut amount in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
