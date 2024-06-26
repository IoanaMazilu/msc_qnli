yhat_premise = 1 + 3 + 3 + 1 = 8
yhat_hypothesis = 7 + 3 + 3 + 1 = 11

# the hypothesis talks about the time Andrew drove at different speeds, which is also mentioned in the premise
if yhat_premise!= yhat_hypothesis:
    # check if the total time Andrew drove at different speeds in the hypothesis contradicts the total time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
