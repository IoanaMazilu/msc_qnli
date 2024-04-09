susan_weight_premise = 40
anna_weight_premise = 40
total_weight_premise = 110

# the hypothesis talks about the weight of Susan and Anna, referenced also in the premise
if susan_weight_hypothesis <= (anna_weight_hypothesis + total_weight_premise):
    # check if the hypothesis value contradicts the estimate of Susan's weight in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of Susan and Anna
    # any weight for Susan that is consistent with the premise is not entailment, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
