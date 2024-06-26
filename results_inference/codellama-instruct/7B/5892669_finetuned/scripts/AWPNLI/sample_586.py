cds_per_shelf_premise = 4.0
cds_hypothesis = 8.0
shelves_hypothesis = 2.0

# the hypothesis refers to the number of CDs and shelves, which are also mentioned in the premise
# compute the total number of shelves needed in the premise
shelves_needed_premise = cds_hypothesis / cds_per_shelf_premise
if shelves_hypothesis!= shelves_needed_premise:
    # check if the number of shelves in the hypothesis contradicts the number of shelves needed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)