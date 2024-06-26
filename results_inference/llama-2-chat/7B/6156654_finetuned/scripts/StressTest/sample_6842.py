# the premise and hypothesis are the same, so we can compare them
if "entailment"!= label:
    # the premise and hypothesis are not contradictory, so we can infer entailment
    label = "entailment"
elif "contradiction"!= label:
    # the premise and hypothesis are not contradictory, so we can infer entailment
    label = "entailment"
else:
    # the premise and hypothesis are contradictory, so we can infer contradiction
    label = "contradiction"

print(label)
