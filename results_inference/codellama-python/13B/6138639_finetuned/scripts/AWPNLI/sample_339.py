feathers_per_crown_premise = 7.0
crowns_hypothesis = 934.0
feathers_hypothesis = 6533.0

# the hypothesis refers to the number of feathers and crowns, which are also mentioned in the premise
# compute the total number of feathers in the premise
total_feathers_premise = crowns_hypothesis * feathers_per_crown_premise
if feathers_hypothesis!= total_feathers_premise:
    # check if the number of feathers in the hypothesis contradicts the number of feathers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
