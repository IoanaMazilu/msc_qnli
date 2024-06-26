power_loss_premise = 125000
killed_hypothesis = 125000

# the hypothesis talks about the number of people killed by a storm, which is also mentioned in the premise
if power_loss_hypothesis == power_loss_premise:
    # if the number of people affected by power loss in the hypothesis matches the number in the premise, we can infer entailment
    label = "entailment"
elif killed_hypothesis!= killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
