# the premise and hypothesis both talk about the same situation (flight departures) and the same rate (on-time departures)

# the hypothesis refers to a different percentage for the on-time departure rate (50%) than the premise (70%)
if percentage_premise == percentage_hypothesis:
    # if the percentage in the hypothesis is the same as the percentage in the premise, we can infer entailment
    label = "entailment"
elif percentage_premise > percentage_hypothesis:
    # if the percentage in the premise is higher than the percentage in the hypothesis, we can infer contradiction
    label = "contradiction"
else:
    # if the percentage in the premise is equal to the percentage in the hypothesis, but not greater, we can infer neutrality
    label = "neutral"

print(label)
