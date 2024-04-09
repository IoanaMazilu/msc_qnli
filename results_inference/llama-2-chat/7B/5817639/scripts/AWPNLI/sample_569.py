dollars_premise = 34.0
dollars_hypothesis = 78.0

# check if the hypothesis value contradicts the premise value
if dollars_hypothesis > dollars_premise:
    label = "contradiction"
elif dollars_hypothesis - dollars_premise < 0:
    label = "entailment"
else:
    label = "neutral"

print(label)
