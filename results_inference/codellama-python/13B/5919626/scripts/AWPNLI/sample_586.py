cds_premise = 4.0
shelves_hypothesis = 2.0
cds_hypothesis = 8.0

# the hypothesis talks about the number of CDs, which are also referenced in the premise
# find the total number of CDs from the premise 
total_cds_premise = cds_premise
if total_cds_hypothesis!= total_cds_premise:
    # check if the number of CDs in the hypothesis contradicts the number of CDs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
