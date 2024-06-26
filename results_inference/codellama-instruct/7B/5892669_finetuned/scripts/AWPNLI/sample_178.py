initial_marbles_premise = 16.0
lost_marbles_premise = 7.0
remaining_marbles_hypothesis = 9.0

# the hypothesis refers to the number of marbles Josh has now, which is also mentioned in the premise
# compute the remaining number of marbles in the premise
remaining_marbles_premise = initial_marbles_premise - lost_marbles_premise
if remaining_marbles_hypothesis!= remaining_marbles_premise:
    # check if the number of marbles in the hypothesis contradicts the number of marbles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
