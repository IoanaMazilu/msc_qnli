cds_per_shelf_premise = 4.0
cds_hypothesis = 8.0
shelves_hypothesis = 4.0

# the hypothesis refers to the number of CDs and shelves, which are also mentioned in the premise
# compute the total number of shelves needed in the hypothesis
shelves_needed_hypothesis = cds_hypothesis / cds_per_shelf_premise
if shelves_needed_hypothesis != shelves_hypothesis:
    # check if the number of shelves in the hypothesis contradicts the number of shelves needed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
