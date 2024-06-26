premise_distance = 5 * 40
hypothesis_distance = 1 * 40

if premise_distance < hypothesis_distance:
    label = "contradiction"
elif premise_distance == hypothesis_distance:
    label = "entailment"
else:
    label = "neutral"

print(label)
