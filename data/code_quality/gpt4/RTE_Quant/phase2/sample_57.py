total_executions_premise = 420
population_premise = 4.4e6
total_executions_hypothesis = 4.4e6

# the hypothesis talks about the total number of people executed in Singapore which is also mentioned in the premise
if total_executions_hypothesis != total_executions_premise:
    # check if the total number of executions in the hypothesis contradicts the number of executions from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
