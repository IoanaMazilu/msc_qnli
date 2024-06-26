executions_premise = 420
population_premise = 4.4e6
executions_hypothesis = 4.4e6

# the hypothesis talks about the number of executions in Singapore, which is also mentioned in the premise
if executions_hypothesis!= executions_premise:
    # check if the number of executions in the hypothesis contradicts the number of executions from the premise
    label = "contradiction"
elif population_hypothesis!= population_premise:
    # check if the population in the hypothesis contradicts the population in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
