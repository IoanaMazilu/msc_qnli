speed_of_bruce_premise = 60
speed_of_bruce_hypothesis = 30
speed_of_bhishma_premise = 20
speed_of_bhishma_hypothesis = 20

# the hypothesis refers to the speed of Bruce and Bhishma mentioned in the premise
if speed_of_bruce_hypothesis >= speed_of_bruce_premise:
    # check if the speed of Bruce in the hypothesis contradicts the speed of Bruce in the premise
    label = "contradiction"
elif speed_of_bhishma_hypothesis!= speed_of_bhishma_premise:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma in the premise
    label = "contradiction"
else:
    # if the speeds of Bruce and Bhishma in the hypothesis are the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
