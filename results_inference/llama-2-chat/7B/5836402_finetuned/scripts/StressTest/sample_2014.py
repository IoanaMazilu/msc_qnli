loss_premise = 6
loss_hypothesis = 2

# the hypothesis refers to the number of years and interest rate mentioned in the premise
if loss_premise <= loss_hypothesis:
    # check if the estimate of 'loss_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
elif loss_hypothesis!= loss_premise * (1 + (4/100)):
    # check if the number of years in the hypothesis contradicts the number of years calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
