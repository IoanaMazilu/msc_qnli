molly_max_premise = 100
molly_max_hypothesis = 400

if molly_max_hypothesis >= molly_max_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)