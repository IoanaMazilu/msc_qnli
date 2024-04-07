# Premise: One hour after Matthew started waking from e to y, a distance of less than 75 km, Johnny started walking along the same road from y to e.
# Hypothesis: One hour after Matthew started waking from e to y, a distance of 45 km, Johnny started walking along the same road from y to e.
# Golden Label: neutral

distance_premise = 75
distance_hypothesis = 45

# the hypothesis talks about the distance from e to y, which is also mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # any distance from e to y less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

