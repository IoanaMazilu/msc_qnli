oil_premise = 8
oil_hypothesis = 7

# the hypothesis talks about the amount of oil needed for each cylinder, which is also mentioned in the premise
if oil_premise <= oil_hypothesis:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
