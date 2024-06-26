switzerland_premise = 3
switzerland_hypothesis = 3
ecuador_premise = 3
ecuador_hypothesis = 3
honduras_premise = 1
honduras_hypothesis = 1

# the hypothesis mentions Ecuador's first win in the group, which is also mentioned in the premise
if ecuador_hypothesis!= ecuador_premise:
    # check if the number of wins for Ecuador in the hypothesis contradicts the number of wins in the premise
    label = "contradiction"
elif honduras_hypothesis!= honduras_premise:
    # check if the number of goals scored by Honduras in the hypothesis contradicts the number of goals scored in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
