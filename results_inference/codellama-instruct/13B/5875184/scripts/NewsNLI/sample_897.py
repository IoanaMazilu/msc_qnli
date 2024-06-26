switzerland_premise = 3
switzerland_hypothesis = 3
ecuador_premise = 3
ecuador_hypothesis = 3
honduras_premise = 1
honduras_hypothesis = 2

# the hypothesis mentions the score of Ecuador against Honduras, which is also mentioned in the premise
if ecuador_hypothesis!= ecuador_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif honduras_hypothesis!= honduras_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
