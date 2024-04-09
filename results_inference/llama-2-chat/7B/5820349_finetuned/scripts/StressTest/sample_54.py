bruce_speed_premise = 30
bruce_speed_hypothesis = 60
bhishma_speed_premise = 20
bhishma_speed_hypothesis = 20

# the hypothesis refers to the speed of Bruce and Bhishma mentioned in the premise
if bruce_speed_premise >= bruce_speed_hypothesis:
    # check if the estimate of 'bruce_speed_hypothesis' contradicts the speed of Bruce in the premise
    label = "contradiction"
elif bhishma_speed_premise!= bhishma_speed_hypothesis:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
