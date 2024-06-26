speed_of_Bruce_premise = 30
speed_of_Bruce_hypothesis = 60
speed_of_Bhishma_premise = 20
speed_of_Bhishma_hypothesis = 20

# the hypothesis talks about the speed of Bruce and Bhishma, which are also mentioned in the premise
if speed_of_Bruce_hypothesis!= speed_of_Bruce_premise:
    # check if the speed of Bruce in the hypothesis contradicts its speed in the premise
    label = "contradiction"
elif speed_of_Bhishma_hypothesis!= speed_of_Bhishma_premise:
    # check if the speed of Bhishma in the hypothesis contradicts its speed in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis and premise match, we can infer entailment
    label = "entailment"

print(label)
