earmuffs_before_december_premise = 6444.0
earmuffs_during_december_premise = 1346.0
earmuffs_sold_in_december_hypothesis = 5100.0

# the hypothesis refers to the number of earmuffs sold in December, which can be calculated from the premise
# the hypothesis value is less than the sum of earmuffs sold before December and during December, which can be calculated from the premise
# the hypothesis value is greater than the number of earmuffs sold before December, which can be calculated from the premise

if earmuffs_sold_in_december_hypothesis <= earmuffs_before_december_premise:
    # check if the hypothesis value is less than or equal to the number of earmuffs sold before December
    label = "entailment"
elif earmuffs_sold_in_december_hypothesis > earmuffs_before_december_premise:
    # check if the hypothesis value is greater than the number of earmuffs sold before December
    label = "contradiction"
else:
    # check if the hypothesis value is equal to the number of earmuffs sold before December
    label = "entailment"

print(label)
