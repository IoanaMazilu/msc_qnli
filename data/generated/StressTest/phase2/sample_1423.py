# Premise: One hour after Yolanda started walking from X to Y, a distance of less than 62 miles, Bob started walking along the same road from Y to X.
# Hypothesis: One hour after Yolanda started walking from X to Y, a distance of 52 miles, Bob started walking along the same road from Y to X.
# Golden Label: neutral

distance_premise = 62
distance_hypothesis = 52

# the hypothesis refers to the distance between two points mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the 'distance_hypothesis' contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # if the distance in the hypothesis is less than the distance in the premise, it is consistent with the premise
    # however, it cannot be explicitly confirmed from the premise that the distance is exactly 'distance_hypothesis', so the relation is neutral
    label = "neutral"

print(label)

