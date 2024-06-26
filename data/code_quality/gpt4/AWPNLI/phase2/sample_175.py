cds_per_rack_premise = 8.0
racks_per_shelf_premise = 4.0
total_cds_hypothesis = 36.0

# The hypothesis states the total number of CDs that can fit on the shelf, which is dependent on the number of racks per shelf and CDs per rack, mentioned in the premise.
# calculate the total number of CDs that can fit on the shelf based on the premise
total_cds_premise = cds_per_rack_premise * racks_per_shelf_premise

if total_cds_hypothesis == total_cds_premise:
    # check if the total number of CDs in the hypothesis matches the total number of CDs from the premise
    label = "entailment"
else:
    # if the total number of CDs in the hypothesis contradicts the total number of CDs from the premise
    label = "contradiction"    

print(label)
