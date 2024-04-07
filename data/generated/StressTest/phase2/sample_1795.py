# Premise: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for less than 8 km each.
# Hypothesis: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for 6 km each.
# Golden Label: neutral

distance_premise = 8
distance_hypothesis = 6

# the hypothesis refers to the distance that the sisters have run, mentioned also in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives an estimate for the distance the sisters have run
    # 'distance_hypothesis' is less than 'distance_premise', so it does not contradict the premise and can be entailed from the premise
    label = "entailment"

print(label)

