speed_of_bruce_premise = 30
speed_of_bruce_hypothesis = 60
speed_of_bhishma_premise = 20
speed_of_bhishma_hypothesis = 20

# the hypothesis talks about the speed of Bruce and Bhishma, which are also mentioned in the premise
if speed_of_bruce_premise < speed_of_bruce_hypothesis:
    # check if the speed of Bruce in the hypothesis contradicts the speed of Bruce in the premise
    label = "contradiction"
elif speed_of_bhishma_hypothesis!= speed_of_bhishma_premise:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
