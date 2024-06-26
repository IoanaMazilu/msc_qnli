speed_Bruce_premise = 60
speed_Bruce_hypothesis = 30
speed_Bhishma_premise = 20
speed_Bhishma_hypothesis = 20

# the hypothesis talks about the speed of Bruce and Bhishma, referenced also in the premise
if speed_Bruce_hypothesis >= speed_Bruce_premise:
    # check if the speed of Bruce in the hypothesis contradicts the estimate of less than'speed_Bruce_premise'
    label = "contradiction"
elif speed_Bhishma_hypothesis!= speed_Bhishma_premise:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
