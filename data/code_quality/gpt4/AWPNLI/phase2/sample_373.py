initial_dimes_premise = 7.0
dimes_given_to_dad_premise = 8.0
dimes_received_from_mom_premise = 4.0
final_dimes_hypothesis = 5.0

# the hypothesis refers to the number of dimes Melanie has now, which we can calculate from the premise
# compute the final number of dimes in the premise
final_dimes_premise = initial_dimes_premise - dimes_given_to_dad_premise + dimes_received_from_mom_premise
if final_dimes_hypothesis != final_dimes_premise:
    # check if the number of dimes in the hypothesis contradicts the final number of dimes from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
