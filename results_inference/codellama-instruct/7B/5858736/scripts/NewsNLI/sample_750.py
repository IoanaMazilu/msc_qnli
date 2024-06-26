bail_premise = 5000000
bail_hypothesis = 1000000

if bail_hypothesis!= bail_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
