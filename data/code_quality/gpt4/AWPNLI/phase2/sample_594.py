pigs_in_barn_premise = 64.0
pigs_join_premise = 86.0
total_pigs_hypothesis = 150.0

# the hypothesis refers to the total number of pigs, which is also calculated in the premise
# compute the total number of pigs in the premise
total_pigs_premise = pigs_in_barn_premise + pigs_join_premise
if total_pigs_hypothesis != total_pigs_premise:
    # check if the total number of pigs in the hypothesis contradicts the total number of pigs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
