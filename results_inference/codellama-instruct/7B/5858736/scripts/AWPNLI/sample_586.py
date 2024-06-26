cds_premise = 4.0
shelves_hypothesis = 2.0
cds_hypothesis = 8.0

# the hypothesis refers to the number of shelves needed to hold a certain number of CDs
# compute the total number of CDs that can fit on a shelf
cds_per_shelf = cds_premise / shelves_hypothesis
if cds_hypothesis <= cds_per_shelf:
    # check if the number of CDs in the hypothesis is less than or equal to the number of CDs that can fit on a shelf
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer contradiction
    label = "contradiction"

print(label)
