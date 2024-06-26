premise = 6
hypothesis = 4

if hypothesis > premise:
    label = "contradiction"
elif hypothesis == premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
