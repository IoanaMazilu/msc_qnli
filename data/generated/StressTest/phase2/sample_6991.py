# Premise: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for less than 52 km each.
# Hypothesis: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for 12 km each.
# Golden Label: neutral

distance_premise = 52
distance_hypothesis = 12

# the hypothesis refers to the distance run by the sisters, which is also mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the distance run by the sisters
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

