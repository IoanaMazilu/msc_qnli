percentage_premise = 0.72
states_hypothesis = 37

# the hypothesis mentions the number of states that allow same-sex marriage, which is also referenced in the premise
if states_hypothesis!= percentage_premise:
    # check if the number of states in the hypothesis contradicts the percentage of states in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
