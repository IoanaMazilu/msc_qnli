money_jones_premise = 0.4
money_jones_hypothesis = 0.6

if money_jones_hypothesis >= money_jones_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
