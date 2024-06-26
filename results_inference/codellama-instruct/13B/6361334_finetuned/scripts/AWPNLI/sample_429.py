earmuffs_before_december_premise = 6444.0
earmuffs_during_december_premise = 1346.0
earmuffs_sold_in_december_hypothesis = 5100.0

# the hypothesis refers to the number of earmuffs sold in December, which are also mentioned in the premise
# compute the total number of earmuffs sold before December
total_earmuffs_before_december_premise = earmuffs_before_december_premise + earmuffs_during_december_premise
if earmuffs_sold_in_december_hypothesis!= total_earmuffs_before_december_premise:
    # check if the number of earmuffs in the hypothesis contradicts the number of earmuffs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
