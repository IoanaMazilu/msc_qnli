# Premise: Connie had 73 marbles and she gave 70.0 to Juan.
# Hypothesis: Connie has 4.0 marbles now.
# Golden Label: contradiction

initial_marbles_connie = 73
given_marbles_premise = 70.0
remaining_marbles_hypothesis = 4.0

# the hypothesis talks about the remaining marbles with Connie, which is also referenced in the premise
# find the remaining marbles with Connie from the premise
remaining_marbles_premise = initial_marbles_connie - given_marbles_premise
if remaining_marbles_hypothesis != remaining_marbles_premise:
    # check if the remaining marbles in the hypothesis contradicts the remaining marbles in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

