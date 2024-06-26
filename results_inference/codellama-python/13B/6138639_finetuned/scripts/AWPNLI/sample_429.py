earmuffs_before_dec_premise = 6444.0
earmuffs_during_dec_premise = 1346.0
earmuffs_during_dec_hypothesis = 5100.0

# the hypothesis refers to the number of earmuffs sold in December, which are also mentioned in the premise
# compute the total number of earmuffs sold in December in the premise
total_earmuffs_during_dec_premise = earmuffs_before_dec_premise - earmuffs_during_dec_premise
if earmuffs_during_dec_hypothesis!= total_earmuffs_during_dec_premise:
    # check if the number of earmuffs sold in December in the hypothesis contradicts the number of earmuffs sold in December from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
