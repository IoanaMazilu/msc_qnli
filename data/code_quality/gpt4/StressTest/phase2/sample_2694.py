shirts_premise = 8
shirts_hypothesis = 2

# the hypothesis talks about the number of shirts Bob is about to hang, referenced also in the premise
if shirts_premise <= shirts_hypothesis:
    # check if the number of shirts in the premise contradicts the estimate of more than 'shirts_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
