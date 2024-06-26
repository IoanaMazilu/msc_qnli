dimes_initial_premise = 7.0
dimes_given_premise = 8.0
dimes_received_premise = 4.0
dimes_final_hypothesis = 3.0

# the hypothesis refers to the total number of dimes Melanie has now, which is also calculated in the premise
# compute the total number of dimes Melanie has after giving and receiving dimes in the premise
dimes_final_premise = dimes_initial_premise - dimes_given_premise + dimes_received_premise
if dimes_final_hypothesis != dimes_final_premise:
    # check if the number of dimes in the hypothesis contradicts the number of dimes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
