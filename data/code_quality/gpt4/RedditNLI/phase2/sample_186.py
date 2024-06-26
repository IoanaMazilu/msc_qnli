GDP_change_premise = -0.7
GDP_change_hypothesis = -0.7

# the hypothesis and premise mention the change in US GDP in the first quarter
if GDP_change_hypothesis != GDP_change_premise:
    # check if the GDP change in the hypothesis contradicts the GDP change in the premise
    label = "contradiction"
else:
    # if the GDP change in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
