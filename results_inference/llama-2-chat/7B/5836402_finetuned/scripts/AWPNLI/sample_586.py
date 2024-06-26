cds_premise = 4.0
shelves_hypothesis = 2.0
cds_hypothesis = 8.0

# the hypothesis refers to the number of shelves, which is also mentioned in the premise
# compute the number of shelves needed to hold the cds in the premise
shelves_premise = cds_premise / 4.0
if shelves_hypothesis!= shelves_premise:
    # check if the number of shelves in the hypothesis contradicts the number of shelves from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
