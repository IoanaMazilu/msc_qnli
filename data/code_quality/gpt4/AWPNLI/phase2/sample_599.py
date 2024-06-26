marbles_initial_premise = 16.0
found_marbles_premise = 7.0
total_marbles_hypothesis = 25.0

# the hypothesis refers to the total number of marbles, which is also discussed in the premise
# compute the total number of marbles in the premise
total_marbles_premise = marbles_initial_premise + found_marbles_premise
if total_marbles_hypothesis != total_marbles_premise:
    # check if the total number of marbles in the hypothesis contradicts the total number of marbles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
