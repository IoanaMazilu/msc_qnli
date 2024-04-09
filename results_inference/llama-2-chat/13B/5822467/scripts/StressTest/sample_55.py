bruce_speed_premise = 60
bruce_speed_hypothesis = 30
bhishma_speed_premise = 20
bhishma_speed_hypothesis = 20

# the hypothesis refers to the speeds of Bruce and Bhishma mentioned in the premise
if bruce_speed_premise <= bruce_speed_hypothesis:
    # check if the estimate of 'bruce_speed_hypothesis' contradicts the speed of Bruce in the premise
    label = "contradiction"
elif bhishma_speed_hypothesis!= bhishma_speed_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
