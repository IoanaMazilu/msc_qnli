agents_premise = 1
agents_hypothesis = 1

# the hypothesis mentions the number of Secret Service agents found intoxicated, which is also referenced in the premise
if agents_hypothesis!= agents_premise:
    # check if the number of agents in the hypothesis contradicts the number of agents reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
