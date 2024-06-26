cds_premise = 4.0
cds_hypothesis = 8.0
shelves_hypothesis = 2.0

# the hypothesis talks about the number of CDs that can fit on shelves, which is also referenced in the premise
# compute the number of shelves needed based on the premise
shelves_premise = cds_hypothesis / cds_premise
if shelves_premise != shelves_hypothesis:
    # check if the number of shelves in the hypothesis contradicts the number of shelves computed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
