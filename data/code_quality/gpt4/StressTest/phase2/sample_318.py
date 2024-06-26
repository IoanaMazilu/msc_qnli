pies_baked_premise = 810
pies_baked_hypothesis = 310

# the hypothesis talks about the number of pies baked by Anitha, referenced also in the premise
if pies_baked_premise <= pies_baked_hypothesis:
    # check if the number of pies baked in the premise contradicts the estimate of more than 'pies_baked_hypothesis'
    label = "contradiction"
else:
    # if the number of pies baked in the premise is greater than 'pies_baked_hypothesis', we can infer entailment
    label = "entailment"

print(label)
