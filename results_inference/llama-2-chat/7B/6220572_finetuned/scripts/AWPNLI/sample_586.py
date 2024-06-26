cds_premise = 4.0
shelves_hypothesis = 2.0
cds_hypothesis = 8.0

# the hypothesis refers to the number of CDs and shelves needed to hold them, which are also referenced in the premise
# compute the number of CDs in the premise
cds_premise = cds_premise / 0.1
if cds_hypothesis!= cds_premise:
    # check if the number of CDs in the hypothesis contradicts the number of CDs from the premise
    label = "contradiction"
elif shelves_hypothesis!= 2.0:
    # check if the number of shelves in the hypothesis contradicts the number of shelves in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
