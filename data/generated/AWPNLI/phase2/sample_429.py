# Premise: Before December, customers bought 6444.0 ear muffs from the mall and During December, they bought 1346.0 less earmuffs than before.
# Hypothesis: 5100.0 earmuffs were sold in December.
# Golden Label: contradiction

earmuffs_before_december_premise = 6444.0
less_earmuffs_december_premise = 1346.0
earmuffs_december_hypothesis = 5100.0

# the hypothesis refers to the number of earmuffs sold in December, which is also inferred in the premise
# compute the number of earmuffs sold in December from the premise
earmuffs_december_premise = earmuffs_before_december_premise - less_earmuffs_december_premise
if earmuffs_december_hypothesis != earmuffs_december_premise:
    # check if the number of earmuffs in the hypothesis contradicts the number of earmuffs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

