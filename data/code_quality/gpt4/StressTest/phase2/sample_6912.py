on_time_rate_premise = 70
on_time_rate_hypothesis = 80

# the hypothesis talks about the on-time departure rate, referenced also in the premise
if on_time_rate_hypothesis != on_time_rate_premise:
    # check if the on-time departure rate in the hypothesis contradicts the on-time departure rate in the premise
    label = "contradiction"
else:
    # if the on-time departure rate in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)
