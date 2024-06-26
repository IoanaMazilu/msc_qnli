earmuffs_premise = 6444.0
earmuffs_difference_premise = 1346.0
earmuffs_hypothesis = 5100.0

# the hypothesis refers to the number of earmuffs sold in December, which is also mentioned in the premise
# compute the number of earmuffs sold in December from the premise
earmuffs_sold_premise = earmuffs_premise - earmuffs_difference_premise
if earmuffs_hypothesis!= earmuffs_sold_premise:
    # check if the number of earmuffs sold in December from the hypothesis contradicts the number of earmuffs sold in December from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
