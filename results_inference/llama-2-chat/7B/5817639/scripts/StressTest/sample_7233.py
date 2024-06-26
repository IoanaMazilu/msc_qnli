twins_sisters_premise = "Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for 2 km each."
twins_sisters_hypothesis = "Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for less than 3 km each."

# the hypothesis talks about the distance the twins sisters ran, referenced also in the premise
if twins_sisters_hypothesis <= twins_sisters_premise:
    # check if the hypothesis value contradicts the estimate of more than 'twins_sisters_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance the twins sisters ran
    # any distance less than 'twins_sisters_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
