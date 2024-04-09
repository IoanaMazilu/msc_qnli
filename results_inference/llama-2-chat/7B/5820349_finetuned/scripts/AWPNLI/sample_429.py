earmuffs_before_dec_premise = 6444.0
earmuffs_difference_dec_premise = 1346.0
earmuffs_sold_dec_hypothesis = 5100.0

# the hypothesis refers to the number of earmuffs sold in December, which is also mentioned in the premise
# compute the total number of earmuffs sold in December in the premise
earmuffs_sold_dec_premise = earmuffs_before_dec_premise - earmuffs_difference_dec_premise
if earmuffs_sold_dec_hypothesis!= earmuffs_sold_dec_premise:
    # check if the number of earmuffs sold in December in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
