# define the variables for the premise and hypothesis
cds_per_shelf_premise = 4.0
cds_hypothesis = 8.0

# the hypothesis refers to the number of shelves needed to hold a certain number of CDs, which is also mentioned in the premise
# compute the number of shelves needed in the premise
shelves_premise = cds_hypothesis / cds_per_shelf_premise

# check if the number of shelves in the hypothesis contradicts the number of shelves from the premise
if cds_hypothesis > cds_per_shelf_premise * shelves_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
 