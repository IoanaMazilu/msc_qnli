earmuffs_before_dec_premise = 6444.0
earmuffs_dec_diff_premise = 1346.0
earmuffs_dec_premise = 5100.0

# the hypothesis refers to the number of earmuffs sold in December, which is also mentioned in the premise
# compute the number of earmuffs sold in December according to the premise
earmuffs_dec_premise_computed = earmuffs_before_dec_premise - earmuffs_dec_diff_premise
if earmuffs_dec_premise!= earmuffs_dec_premise_computed:
    # check if the number of earmuffs sold in December according to the hypothesis contradicts the number computed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
