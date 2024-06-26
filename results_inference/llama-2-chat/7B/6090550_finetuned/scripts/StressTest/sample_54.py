y_Bruce_speed_premise = 30
y_Bhishma_speed_premise = 20
y_Bruce_speed_hypothesis = 60
y_Bhishma_speed_hypothesis = 20

# the hypothesis talks about the speed of Bruce and Bhishma, referenced also in the premise
if y_Bruce_speed_premise >= y_Bruce_speed_hypothesis:
    # check if the hypothesis speed of Bruce contradicts the speed of Bruce in the premise
    label = "contradiction"
elif y_Bhishma_speed_premise!= y_Bhishma_speed_hypothesis:
    # check if the hypothesis speed of Bhishma contradicts the speed of Bhishma in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

