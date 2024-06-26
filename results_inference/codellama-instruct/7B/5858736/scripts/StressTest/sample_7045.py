raman_travelled_premise = 20
raman_travelled_hypothesis = 10

if raman_travelled_hypothesis >= raman_travelled_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
