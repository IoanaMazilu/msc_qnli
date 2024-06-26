earmuffs_sold_before_december_premise = 6444.0
earmuffs_sold_december_premise = 1346.0
earmuffs_sold_december_hypothesis = 5100.0

# the hypothesis refers to the number of earmuffs sold in December, which is also mentioned in the premise
# compute the number of earmuffs sold in December according to the premise
earmuffs_sold_december_premise = earmuffs_sold_before_december_premise - earmuffs_sold_december_premise
if earmuffs_sold_december_hypothesis!= earmuffs_sold_december_premise:
    # check if the number of earmuffs sold in December according to the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
