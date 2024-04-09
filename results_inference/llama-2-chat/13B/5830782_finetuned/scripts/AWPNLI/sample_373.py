dimes_melanie_premise = 7.0
dimes_given_dad_premise = 8.0
dimes_given_mom_premise = 4.0
dimes_hypothesis = 5.0

# the hypothesis refers to the number of dimes Melanie has now, which is also mentioned in the premise
# compute the total number of dimes Melanie has now in the premise
total_dimes_premise = dimes_melanie_premise + dimes_given_dad_premise - dimes_given_mom_premise
if dimes_hypothesis!= total_dimes_premise:
    # check if the number of dimes in the hypothesis contradicts the number of dimes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
