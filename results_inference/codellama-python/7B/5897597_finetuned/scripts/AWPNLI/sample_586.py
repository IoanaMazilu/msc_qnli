cds_per_shelf_premise = 4.0
shelves_hypothesis = 2.0
cds_hypothesis = 8.0

# the hypothesis refers to the number of CDs and shelves needed, which are also mentioned in the premise
# compute the total number of CDs that can fit on a shelf in the premise
total_cds_premise = cds_per_shelf_premise * shelves_hypothesis
if cds_hypothesis!= total_cds_premise:
    # check if the number of CDs in the hypothesis contradicts the number of CDs that can fit on a shelf from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
