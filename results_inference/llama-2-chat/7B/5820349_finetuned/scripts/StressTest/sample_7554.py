cleaning_time_premise = 6
cleaning_time_hypothesis = 1

# the hypothesis refers to the time Jim takes to clean the house, mentioned in the premise
if cleaning_time_premise <= cleaning_time_hypothesis:
    # check if the cleaning time in the premise contradicts the estimate of'more than cleaning_time_hypothesis'
    label = "contradiction"
else:
    # if the cleaning time in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
