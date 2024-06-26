shoes_marcella_premise = 65
shoes_marcella_hypothesis = 25

if shoes_marcella_hypothesis >= shoes_marcella_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
