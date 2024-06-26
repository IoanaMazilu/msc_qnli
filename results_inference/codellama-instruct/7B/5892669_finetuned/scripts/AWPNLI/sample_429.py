earmuffs_bought_before_dec_premise = 6444.0
earmuffs_bought_dec_diff_premise = 1346.0
earmuffs_sold_dec_hypothesis = 5100.0

# the hypothesis refers to the number of earmuffs sold in December, which is also mentioned in the premise
# compute the total number of earmuffs sold in December from the premise
earmuffs_sold_dec_premise = earmuffs_bought_before_dec_premise - earmuffs_bought_dec_diff_premise
if earmuffs_sold_dec_hypothesis!= earmuffs_sold_dec_premise:
    # check if the number of earmuffs sold in December in the hypothesis contradicts the number of earmuffs sold in December from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
