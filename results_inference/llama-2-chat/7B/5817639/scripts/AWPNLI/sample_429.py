before_december_earmuffs_premise = 6444.0
during_december_earmuffs_premise = 1346.0
entire_earmuffs_hypothesis = 5100.0

# compare the number of earmuffs sold during December with the number sold before December
if during_december_earmuffs_premise!= (entire_earmuffs_hypothesis - before_december_earmuffs_premise):
    # if the number of earmuffs sold during December contradicts the number sold before December
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
