dimes_melanie_premise = 7.0
dimes_dad_premise = 8.0
dimes_mom_premise = 4.0
total_dimes_hypothesis = 18.0

# the hypothesis refers to the total number of dimes Melanie has, which is also mentioned in the premise
# compute the total number of dimes Melanie has in the premise
total_dimes_premise = dimes_melanie_premise + dimes_dad_premise + dimes_mom_premise
if total_dimes_hypothesis!= total_dimes_premise:
    # check if the total number of dimes in the hypothesis contradicts the total number of dimes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)