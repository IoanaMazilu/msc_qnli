distance_premise = 15
distance_hypothesis = float(input("Enter the distance between West-Town and East-Town: "))

# check if the hypothesis value contradicts the premise value
if distance_hypothesis > distance_premise:
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    label = "neutral"
else:
    # the hypothesis value is consistent with the premise value, so we can infer entailment
    label = "entailment"

print(label)
