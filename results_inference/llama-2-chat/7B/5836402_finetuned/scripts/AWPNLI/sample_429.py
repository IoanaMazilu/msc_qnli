before_muffs_premise = 6444.0
less_muffs_premise = 1346.0
total_muffs_hypothesis = 5100.0

# the hypothesis refers to the total number of earmuffs sold in December, which is also mentioned in the premise
# compute the total number of earmuffs sold in December from the premise
total_muffs_premise = before_muffs_premise - less_muffs_premise
if total_muffs_hypothesis!= total_muffs_premise:
    # check if the number of earmuffs sold in December from the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
