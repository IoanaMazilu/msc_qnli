expert_premise = 1
expert_hypothesis = 1

if expert_hypothesis!= expert_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
