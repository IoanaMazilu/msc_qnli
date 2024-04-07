# Premise: One hour after Yolanda started walking from X to Y, a distance of less than 81 miles, Bob started walking along the same road from Y to X.
# Hypothesis: One hour after Yolanda started walking from X to Y, a distance of 31 miles, Bob started walking along the same road from Y to X.
# Golden Label: neutral

distance_premise = 81
distance_hypothesis = 31

# the hypothesis refers to the same distance from X to Y as the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    label = "entailment"

print(label)

