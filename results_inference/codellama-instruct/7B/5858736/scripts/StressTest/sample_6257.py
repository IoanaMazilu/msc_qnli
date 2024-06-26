saren_discount_premise = 20
saren_discount_hypothesis = 50

if saren_discount_hypothesis <= saren_discount_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
