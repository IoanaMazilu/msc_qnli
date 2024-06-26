yhat_premise = 3
yhat_hypothesis = 4

# the hypothesis talks about the number of fastest horses the London Racetrack needs to submit to the Kentucky Derby, which is also mentioned in the premise
if yhat_hypothesis!= yhat_premise:
    # check if the number of fastest horses in the hypothesis contradicts the number of fastest horses in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
