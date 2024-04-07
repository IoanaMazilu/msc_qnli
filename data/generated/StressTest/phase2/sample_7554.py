# Premise: Jim alone cleans the entire house in 6 hours.
# Hypothesis: Jim alone cleans the entire house in more than 1 hours.
# Golden Label: entailment

cleaning_time_premise = 6
cleaning_time_hypothesis = 1

# the hypothesis refers to the time it takes for Jim to clean the house, also mentioned in the premise
if cleaning_time_premise <= cleaning_time_hypothesis:
    # check if the cleaning time in the premise contradicts the estimate of more than 'cleaning_time_hypothesis'
    label = "contradiction"
else:
    # if the premise's cleaning time does not contradict the hypothesis's estimate, we can infer entailment
    label = "entailment"

print(label)

