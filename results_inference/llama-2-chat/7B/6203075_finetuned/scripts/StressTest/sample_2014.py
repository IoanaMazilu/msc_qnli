interest_rate = 4
years = 6

loss_premise = years * (1 + interest_rate) ** years
loss_hypothesis = years * (1 + interest_rate) ** years

# the hypothesis talks about the same situation as the premise, but with different years
if loss_hypothesis!= loss_premise:
    # check if the loss in the hypothesis contradicts the loss in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
