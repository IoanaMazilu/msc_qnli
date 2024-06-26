death_rate_premise = 0.10
death_rate_hypothesis = 0.10

# the hypothesis refers to the death rate of a village in Sri Lanka, also mentioned in the premise
if death_rate_premise <= death_rate_hypothesis:
    # check if the estimate of 'death_rate_hypothesis' contradicts the death rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
