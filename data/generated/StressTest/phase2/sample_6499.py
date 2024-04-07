# Premise: One hour after Matthew started waking from t to y, a distance of more than 35 km, Johnny started walking along the same road from y to t.
# Hypothesis: One hour after Matthew started waking from t to y, a distance of 45 km, Johnny started walking along the same road from y to t.
# Golden Label: neutral

distance_premise = 35
distance_hypothesis = 45

# the hypothesis talks about the same distance from t to y mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

