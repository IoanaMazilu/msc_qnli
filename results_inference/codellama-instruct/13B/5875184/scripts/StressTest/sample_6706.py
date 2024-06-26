premise_ratio = 8/3/1
hypothesis_ratio = 4/3/1

if premise_ratio < hypothesis_ratio:
    label = "contradiction"
elif premise_ratio == hypothesis_ratio:
    label = "entailment"
else:
    label = "neutral"

print(label)
