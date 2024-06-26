speed_bruce_premise = 30
speed_bruce_hypothesis = 60
speed_bhishma_premise = 20
speed_bhishma_hypothesis = 20

# the hypothesis refers to the speed of Bruce and Bhishma mentioned in the premise
if speed_bruce_hypothesis!= speed_bruce_premise:
    # check if the speed of Bruce in the hypothesis contradicts the speed of Bruce reported in the premise
    label = "contradiction"
elif speed_bhishma_hypothesis!= speed_bhishma_premise:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
