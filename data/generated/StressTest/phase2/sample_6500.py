# Premise: One hour after Matthew started waking from t to y, a distance of 45 km, Johnny started walking along the same road from y to t.
# Hypothesis: One hour after Matthew started waking from t to y, a distance of more than 45 km, Johnny started walking along the same road from y to t.
# Golden Label: contradiction

distance_walked_premise = 45
distance_walked_hypothesis = 45

# the hypothesis talks about the distance walked by Matthew which is also referenced in the premise
if distance_walked_hypothesis > distance_walked_premise:
    # check if the hypothesis value contradicts the distance walked in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

