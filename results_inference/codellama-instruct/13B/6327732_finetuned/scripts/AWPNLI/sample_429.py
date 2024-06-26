premise_before_december = 6444.0
premise_during_december = 1346.0
hypothesis_december = 5100.0

# the hypothesis refers to the number of earmuffs sold in December, which is also mentioned in the premise
# compute the total number of earmuffs sold before December
total_earmuffs_before_december = premise_before_december + premise_during_december
if total_earmuffs_before_december!= hypothesis_december:
    # check if the number of earmuffs in the hypothesis contradicts the number of earmuffs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
