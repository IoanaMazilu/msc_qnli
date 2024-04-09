tax_cut_premise = 300e9
tax_cut_hypothesis = 300e9

# the hypothesis and premise mention the value of the tax cut coming from Obama
if tax_cut_hypothesis!= tax_cut_premise:
    # check if the value of the tax cut in the hypothesis contradicts the value of the tax cut in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
