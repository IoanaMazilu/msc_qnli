# Premise: If Packard reads at a constant rate of 4 pages every 5 minutes, how many seconds will it take him to read N pages?
# Hypothesis: If Packard reads at a constant rate of more than 1 pages every 5 minutes, how many seconds will it take him to read N pages?
# Golden Label: entailment

reading_rate_premise = 4
reading_rate_hypothesis = 1

# the hypothesis refers to the reading rate of Packard mentioned in the premise
if reading_rate_premise <= reading_rate_hypothesis:
    # check if the hypothesis value contradicts the reading rate in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

