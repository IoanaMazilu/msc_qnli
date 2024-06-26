dimes_initial_premise = 7.0
dimes_given_premise = 8.0
dimes_received_premise = 4.0
dimes_now_hypothesis = 5.0

# the hypothesis refers to the number of dimes Melanie has now, which is also mentioned in the premise
# compute the total number of dimes Melanie has now in the premise
dimes_now_premise = dimes_initial_premise - dimes_given_premise + dimes_received_premise
if dimes_now_hypothesis!= dimes_now_premise:
    # check if the number of dimes now in the hypothesis contradicts the number of dimes now from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
