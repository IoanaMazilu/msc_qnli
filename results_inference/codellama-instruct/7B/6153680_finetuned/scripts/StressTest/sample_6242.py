ratio_premise = 144/25
ratio_hypothesis = 244/25
BC_premise = 13
BC_hypothesis = 13

# the hypothesis refers to the same ratio and BC as the premise
if ratio_hypothesis!= ratio_premise:
    label = "contradiction"
elif BC_hypothesis!= BC_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
