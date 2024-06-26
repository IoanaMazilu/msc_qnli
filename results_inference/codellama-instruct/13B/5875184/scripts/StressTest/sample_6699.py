premise = 4500
hypothesis = 6500

if premise < hypothesis:
    label = "contradiction"
elif premise == hypothesis:
    label = "neutral"
else:
    label = "entailment"

print(label)
