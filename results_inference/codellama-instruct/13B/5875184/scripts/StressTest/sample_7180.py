premise_distance = 5 * 42
hypothesis_distance = 1 * 42 + 3 * 60

if premise_distance <= hypothesis_distance:
    label = "entailment"
elif premise_distance > hypothesis_distance:
    label = "contradiction"
else:
    label = "neutral"

print(label)
