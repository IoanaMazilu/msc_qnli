# Premise: One hour after Yolanda started walking from X to Y, a distance of less than 30 miles, Bob started walking along the same road from Y to X.
# Hypothesis: One hour after Yolanda started walking from X to Y, a distance of 10 miles, Bob started walking along the same road from Y to X.
# Golden Label: neutral

distance_walked_premise = 30
distance_walked_hypothesis = 10

# the hypothesis refers to the distance walked from X to Y, also mentioned in the premise
if distance_walked_hypothesis >= distance_walked_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_walked_premise'
    label = "contradiction"
elif distance_walked_hypothesis < distance_walked_premise:
    # the premise gives only an estimate for the distance of less than 'distance_walked_premise'
    # any distance less than 'distance_walked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

