bruce_speed_premise = 60
bruce_speed_hypothesis = 30
bhishma_speed_premise = 20
bhishma_speed_hypothesis = 20

# the hypothesis refers to the speed of Bruce and Bhishma mentioned in the premise
if bruce_speed_hypothesis >= bruce_speed_premise:
    # check if the speed of Bruce in the hypothesis contradicts the speed of Bruce in the premise
    label = "contradiction"
elif bhishma_speed_hypothesis!= bhishma_speed_premise:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
