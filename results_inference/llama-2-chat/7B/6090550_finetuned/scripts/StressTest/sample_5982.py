if y_hypothesis >= y_premise:
    label = "contradiction"
elif y_hypothesis < y_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
