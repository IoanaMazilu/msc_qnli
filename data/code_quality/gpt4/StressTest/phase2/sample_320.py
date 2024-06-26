pies_baked_premise = 810
pies_baked_hypothesis = 510

# the hypothesis talks about the number of pies baked by Anitha, referenced also in the premise
if pies_baked_hypothesis != pies_baked_premise:
    # check if the number of pies baked in the hypothesis contradicts the number of pies baked reported in the premise
    label = "contradiction"
else:
    # if the number of pies baked in the hypothesis matches with the premise, we can infer entailment
    label = "entailment"

print(label)
