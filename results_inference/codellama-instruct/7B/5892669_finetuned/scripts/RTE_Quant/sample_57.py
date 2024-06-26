execution_rate_premise = 4.4e6
execution_rate_hypothesis = 4.4e6

# the hypothesis talks about the number of people executed in Singapore, which is also mentioned in the premise
if execution_rate_hypothesis!= execution_rate_premise:
    # check if the execution rate in the hypothesis contradicts the execution rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
