y = 77 kg
kg_mixed_premise = 27 kg

# the hypothesis talks about the weight of butter mixed by Raman, which is also mentioned in the premise
if kg_mixed_premise!= y:
    # check if the weight of butter mixed in the premise contradicts the weight of butter mixed in the hypothesis
    label = "contradiction"
else:
    # if the weight of butter mixed in the premise equals the weight of butter mixed in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
