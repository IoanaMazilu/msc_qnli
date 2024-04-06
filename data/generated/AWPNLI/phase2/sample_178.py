# Premise: Josh had 16.0 marbles in his collection and he lost 7.0 marbles.
# Hypothesis: He has 9.0 marbles now.
# Golden Label: entailment

initial_marbles_premise = 16.0
lost_marbles_premise = 7.0
current_marbles_hypothesis = 9.0

# the hypothesis refers to the number of marbles now, which is also mentioned in the premise
# compute the total number of marbles in the premise
current_marbles_premise = initial_marbles_premise - lost_marbles_premise
if current_marbles_hypothesis != current_marbles_premise:
    # check if the number of marbles in the hypothesis contradicts the number of marbles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

