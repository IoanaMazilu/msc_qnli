# Premise: One hour after Matthew started waking from t to y, a distance of 45 km, Johnny started walking along the same road from y to t.
# Hypothesis: One hour after Matthew started waking from t to y, a distance of more than 35 km, Johnny started walking along the same road from y to t.
# Golden Label: entailment

distance_walked_premise = 45
distance_walked_hypothesis = 35

# the hypothesis talks about the distance between t to y, referenced also in the premise
if distance_walked_hypothesis >= distance_walked_premise:
    # check if the hypothesis value contradicts the exact distance 'distance_walked_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than or equal to the premise value, we can infer entailment
    label = "entailment"

print(label)

