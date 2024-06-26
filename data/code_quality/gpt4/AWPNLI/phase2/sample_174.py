cds_per_rack_premise = 8.0
racks_per_shelf_premise = 4.0
total_cds_hypothesis = 32.0

# the hypothesis refers to the total number of CDs that can fit on the shelf, which can be calculated from the premise
# compute the total number of cds that can fit on the shelf in the premise
total_cds_premise = cds_per_rack_premise * racks_per_shelf_premise
if total_cds_hypothesis != total_cds_premise:
    # check if the number of cds in the hypothesis contradicts the number of cds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
