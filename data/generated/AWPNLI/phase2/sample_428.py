# Premise: Before December, customers bought 6444.0 ear muffs from the mall and During December, they bought 1346.0 less earmuffs than before.
# Hypothesis: 5098.0 earmuffs were sold in December.
# Golden Label: entailment

earmuffs_sold_before_dec_premise = 6444.0
earmuffs_sold_dec_diff_premise = 1346.0
earmuffs_sold_dec_hypothesis = 5098.0

# the hypothesis refers to the number of earmuffs sold in December, which is also mentioned in the premise
# compute the number of earmuffs sold in December according to the premise
earmuffs_sold_dec_premise = earmuffs_sold_before_dec_premise - earmuffs_sold_dec_diff_premise
if earmuffs_sold_dec_hypothesis != earmuffs_sold_dec_premise:
    # check if the number of earmuffs sold in December according to the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

