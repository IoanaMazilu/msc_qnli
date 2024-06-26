premise_feathers = 7.0
premise_crowns = 934.0
hypothesis_feathers = 6533.0
hypothesis_crowns = 934.0

# the hypothesis refers to the number of feathers and crowns, which are also mentioned in the premise
# compute the total number of feathers needed for the premise
total_feathers_premise = premise_feathers * premise_crowns
if total_feathers_premise!= hypothesis_feathers:
    # check if the number of feathers in the hypothesis contradicts the number of feathers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
