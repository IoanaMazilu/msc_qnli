miami_passengers_premise = 7/3 * kennedy_passengers_premise
kennedy_passengers_premise = 4 * logan_passengers_premise
logan_passengers_premise = 4

miami_passengers_hypothesis = 1/3 * kennedy_passengers_hypothesis
kennedy_passengers_hypothesis = 4 * logan_passengers_hypothesis
logan_passengers_hypothesis = 4

# check if the hypothesis values and estimates do not contradict the premise ones
if miami_passengers_premise <= miami_passengers_hypothesis and \
   kennedy_passengers_premise <= kennedy_passengers_hypothesis and \
   logan_passengers_premise <= logan_passengers_hypothesis:
    # no contradiction, so we can infer entailment
    label = "entailment"
elif kennedy_passengers_hypothesis!= kennedy_passengers_premise or \
     logan_passengers_hypothesis!= logan_passengers_premise:
    # at least one aspect in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, but we cannot explicitly entail the hypothesis from the premise
    label = "neutral"

print(label)
