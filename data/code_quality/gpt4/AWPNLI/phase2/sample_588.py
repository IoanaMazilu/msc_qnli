marbles_start_premise = 73
given_marbles_premise = 70.0
remaining_marbles_hypothesis = 3.0

# the hypothesis refers to the number of marbles Connie has now, which are also mentioned in the premise
# compute the remaining number of marbles in the premise
remaining_marbles_premise = marbles_start_premise - given_marbles_premise
if remaining_marbles_hypothesis != remaining_marbles_premise:
    # check if the number of remaining marbles in the hypothesis contradicts the number of remaining marbles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
