# Premise: One hour after Yolanda started walking from X to Y, a distance of less than 74 miles, Bob started walking along the same road from Y to X.
# Hypothesis: One hour after Yolanda started walking from X to Y, a distance of 24 miles, Bob started walking along the same road from Y to X.
# Golden Label: neutral

distance_premise = 74
distance_hypothesis = 24

# the hypothesis refers to the same distance between X and Y as the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

