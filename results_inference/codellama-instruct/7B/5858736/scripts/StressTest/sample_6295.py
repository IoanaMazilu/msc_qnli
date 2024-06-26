money_given_premise = 60
money_given_hypothesis = 40

if money_given_hypothesis >= money_given_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
