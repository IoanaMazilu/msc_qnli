sisters_premise = "Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for 2 km each."
sisters_hypothesis = "Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for 3 km each."

# the hypothesis refers to the distance run by the twins in the premise
if sisters_hypothesis <= sisters_premise:
    # check if the estimate of'sisters_hypothesis' contradicts the distance run in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance run
    # any distance greater than'sisters_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
