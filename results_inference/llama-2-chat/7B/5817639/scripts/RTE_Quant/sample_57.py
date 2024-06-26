people_executed_premise = 420
people_executed_hypothesis = 4.4e6

# the hypothesis talks about a much larger number of executions than the premise, which is a factual statement
if people_executed_hypothesis!= people_executed_premise:
    # check if the number of executions in the hypothesis contradicts the number of executions from the premise
    label = "contradiction"
elif people_executed_hypothesis > people_executed_premise:
    # check if the number of executions in the hypothesis is greater than the number of executions in the premise, which is not possible
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
