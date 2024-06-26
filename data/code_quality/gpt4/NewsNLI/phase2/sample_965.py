imprisoned_agents_premise = 5
imprisoned_agents_hypothesis = 3

# the hypothesis mentions the number of imprisoned Cuban spies, which is also referenced in the premise
if imprisoned_agents_hypothesis > imprisoned_agents_premise:
    # check if the number of imprisoned spies in the hypothesis contradicts the number of imprisoned spies reported in the premise
    label = "contradiction"
else:
    # if the number of imprisoned spies in the hypothesis does not contradict the number of imprisoned spies in the premise, we can infer entailment
    label = "entailment"

print(label)
