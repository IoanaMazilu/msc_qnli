fine_premise = 8000
fine_hypothesis = 8000

if fine_hypothesis!= fine_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
