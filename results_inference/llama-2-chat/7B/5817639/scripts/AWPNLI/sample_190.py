lost_crayons_hypothesis = 345.0
total_crayons_premise = 479.0 + 134.0 = 613.0

if lost_crayons_hypothesis >= total_crayons_premise:
    label = "contradiction"
elif lost_crayons_hypothesis!= total_crayons_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
