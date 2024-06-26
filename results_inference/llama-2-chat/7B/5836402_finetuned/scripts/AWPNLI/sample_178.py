marbles_initial_premise = 16.0
lost_marbles_premise = 7.0
marbles_hypothesis = 9.0

# the hypothesis refers to the current number of marbles, which can be computed from the premise
# compute the current number of marbles in the premise
current_marbles_premise = marbles_initial_premise - lost_marbles_premise
if marbles_hypothesis!= current_marbles_premise:
    # check if the number of marbles in the hypothesis contradicts the number of marbles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
