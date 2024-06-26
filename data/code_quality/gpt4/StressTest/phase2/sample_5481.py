average_shirts_premise = 60
average_shirts_hypothesis = 50
shirts_purchased_each = 6

# the hypothesis talks about the average number of shirts with the three individuals, which is also mentioned in the premise
if average_shirts_premise <= average_shirts_hypothesis:
    # check if the estimate of 'average_shirts_hypothesis' contradicts the average number of shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
