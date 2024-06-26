premise = 48
hypothesis = 18

if premise - hypothesis > 0:
    label = "entailment"
elif premise - hypothesis == 0:
    label = "neutral"
else:
    label = "contradiction"

print(label)
