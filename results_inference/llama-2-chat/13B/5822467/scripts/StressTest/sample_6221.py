ratio_premise = 2:4:8
ratio_hypothesis = less than 2:4:8

# convert the ratios to floats for comparison
ratio_premise_float = float(ratio_premise[0]) / float(ratio_premise[1])
ratio_hypothesis_float = float(ratio_hypothesis[0]) / float(ratio_hypothesis[1])

# compare the ratios
if ratio_premise_float <= ratio_hypothesis_float:
    # the hypothesis ratio is less than or equal to the premise ratio, so there is no contradiction
    label = "neutral"
elif ratio_hypothesis_float!= ratio_premise_float:
    # the hypothesis ratio is not equal to the premise ratio, so there is a contradiction
    label = "contradiction"
else:
    # the hypothesis ratio is equal to the premise ratio, so there is entailment
    label = "entailment"

print(label)
