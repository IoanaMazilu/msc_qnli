initial_marbles_premise = 87.0
received_marbles_premise = 8.0
total_marbles_hypothesis = 95.0

# the hypothesis refers to the total number of marbles, which is also computed in the premise
# calculate total number of marbles in the premise
total_marbles_premise = initial_marbles_premise + received_marbles_premise
if total_marbles_hypothesis != total_marbles_premise:
    # check if the total number of marbles in the hypothesis contradicts the total number of marbles in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
