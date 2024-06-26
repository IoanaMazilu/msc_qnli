withdrawal_premise = 14000
withdrawal_hypothesis = 14000
time_premise = 8
time_hypothesis = 8

# the hypothesis talks about the withdrawal amount and time, which are also mentioned in the premise
if withdrawal_hypothesis >= withdrawal_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif time_hypothesis!= time_premise:
    # check if the time in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
