speed_of_bruce_premise = 60
speed_of_bruce_hypothesis = 30
speed_of_bhishma_premise = 20
speed_of_bhishma_hypothesis = 20

# the hypothesis refers to the speed of two characters, Bruce and Bhishma, mentioned in the premise
if speed_of_bruce_hypothesis >= speed_of_bruce_premise:
    # check if the estimate of'speed_of_bruce_hypothesis' contradicts the speed of Bruce in the premise
    label = "contradiction"
elif speed_of_bhishma_hypothesis!= speed_of_bhishma_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
