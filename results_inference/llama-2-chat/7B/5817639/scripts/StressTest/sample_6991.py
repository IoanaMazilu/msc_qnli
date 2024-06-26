sisters_premise = "Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for less than 52 km each."
sisters_hypothesis = "Two twins sisters Sita and Geeta were standing back to back and suddenly they started running in opposite directions for 12 km each."

# the hypothesis talks about the distance each twin sister ran, which is also mentioned in the premise
if abs(sisters_hypothesis - sisters_premise) <= 12:
    # check if the hypothesis value contradicts the estimate of less than'sisters_premise'
    label = "entailment"
else:
    # the premise gives only an estimate for the distance each twin sister ran
    # any distance greater than or equal to'sisters_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
