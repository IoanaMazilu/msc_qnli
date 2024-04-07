# Premise: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for more than 5 km each.
# Hypothesis: Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for 8 km each.
# Golden Label: neutral

distance_ran_premise = 5
distance_ran_hypothesis = 8

# the hypothesis talks about the distance ran by the twins, referenced also in the premise
if distance_ran_hypothesis <= distance_ran_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_ran_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance ran by the twins
    # any distance greater than 'distance_ran_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

