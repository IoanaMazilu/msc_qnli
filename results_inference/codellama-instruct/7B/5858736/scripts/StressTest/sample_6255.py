saren_discount_premise = 20
saren_discount_hypothesis = 30

if saren_discount_hypothesis >= saren_discount_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
