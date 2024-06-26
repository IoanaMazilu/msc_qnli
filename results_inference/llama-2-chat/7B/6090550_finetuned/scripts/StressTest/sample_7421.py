yhat_premise = 11
yhat_hypothesis = 81

# the hypothesis talks about the floor David gets on and the rate of elevator travel, which are also mentioned in the premise
if yhat_premise!= yhat_hypothesis:
    # check if the hypothesis floor number and rate of elevator travel contradict the ones in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
