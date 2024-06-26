total_marbles_premise = 9.0
given_marbles_premise = 3.0
remaining_marbles_hypothesis = 6.0

# the hypothesis refers to the number of marbles left with Mary, which can be calculated from the premise
# compute the remaining marbles in the premise
remaining_marbles_premise = total_marbles_premise - given_marbles_premise
if remaining_marbles_hypothesis != remaining_marbles_premise:
    # check if the number of remaining marbles in the hypothesis contradicts the number of remaining marbles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
