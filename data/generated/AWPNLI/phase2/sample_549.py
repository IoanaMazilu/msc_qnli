# Premise: Cade had 87.0 marbles and he got 8.0 from Dylan.
# Hypothesis: He has 98.0 marbles now.
# Golden Label: contradiction

marbles_initial_premise = 87.0
marbles_received_premise = 8.0
total_marbles_hypothesis = 98.0

# the hypothesis refers to the total number of marbles, which is also referenced in the premise
# compute the total number of marbles in the premise
total_marbles_premise = marbles_initial_premise + marbles_received_premise
if total_marbles_hypothesis != total_marbles_premise:
    # check if the total number of marbles in the hypothesis contradicts the total number of marbles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

