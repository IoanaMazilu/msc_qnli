cds_per_shelf_premise = 4.0
shelves_needed_hypothesis = 2.0
cds_needed_hypothesis = 8.0

# the hypothesis refers to the number of shelves and CDs, which are also mentioned in the premise
# compute the total number of CDs that can fit on a shelf
total_cds_per_shelf = cds_per_shelf_premise * shelves_needed_hypothesis
if total_cds_per_shelf < cds_needed_hypothesis:
    # check if the number of CDs in the hypothesis contradicts the number of CDs that can fit on a shelf
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
