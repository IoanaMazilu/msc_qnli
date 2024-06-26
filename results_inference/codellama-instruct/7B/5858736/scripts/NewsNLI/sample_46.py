death_premise = 1
injuries_premise = 10

death_hypothesis = 1
injuries_hypothesis = 10

if death_hypothesis!= death_premise:
    label = "contradiction"
elif injuries_hypothesis!= injuries_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
