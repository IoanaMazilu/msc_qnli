y_Bruce_premise = 30
y_Bhishma_premise = 20
y_Bruce_hypothesis = 60
y_Bhishma_hypothesis = 20

# the hypothesis talks about the speed of Bruce and Bhishma, which are also mentioned in the premise
# compute the speeds in the hypothesis
y_Bruce_hypothesis = 30
y_Bhishma_hypothesis = 20

if y_Bruce_hypothesis!= y_Bruce_premise:
    # check if the speed of Bruce in the hypothesis contradicts the speed of Bruce in the premise
    label = "contradiction"
elif y_Bhishma_hypothesis!= y_Bhishma_premise:
    # check if the speed of Bhishma in the hypothesis contradicts the speed of Bhishma in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer entailment
    label = "entailment"

print(label)
