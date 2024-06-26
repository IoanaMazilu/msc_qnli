distance_premise = 450
distance_hypothesis = 150

# The hypothesis talks about the distance between Jack and Christina, also referenced in the premise
if distance_hypothesis > distance_premise:
    # check if the hypothesis value contradicts the estimate of 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value matches the premise, then we can infer entailment
    label = "entailment"

print(label)
