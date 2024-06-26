agent_premise = 1
agent_hypothesis = 1

# the hypothesis mentions the number of Secret Service agents found drunk, which is also referenced in the premise
if agent_hypothesis!= agent_premise:
    # check if the number of agents in the hypothesis contradicts the number of agents reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
